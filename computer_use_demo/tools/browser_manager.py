
import asyncio
import os
from pathlib import Path
from typing import Optional

class BrowserManager:
    def __init__(self):
        self.process: Optional[asyncio.subprocess.Process] = None
        self.display_num = int(os.getenv("DISPLAY_NUM", "0"))
        self._display_prefix = f"DISPLAY=:{self.display_num} "
        self.status = "stopped"
        self.current_url = None
        
    async def start(self):
        if self.process:
            return
            
        try:
            # Start Firefox with specific window position and size
            # Start Xvfb first
            xvfb_cmd = ["Xvfb", f":{self.display_num}", "-screen", "0", "1024x768x24"]
            await asyncio.create_subprocess_exec(*xvfb_cmd)
            await asyncio.sleep(1)  # Wait for Xvfb to start
            
            # Then start Firefox using absolute path
            firefox_path = "/nix/store/firefox-esr/bin/firefox-esr"
            self.process = await asyncio.create_subprocess_exec(
                firefox_path,  # Use absolute path to firefox-esr
                "--width=800",
                "--height=600",
                "about:blank",
                env={"DISPLAY": f":{self.display_num}"},
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            self.status = "running"
        except Exception as e:
            self.status = f"error: {str(e)}"
            raise
            
    async def stop(self):
        if self.process:
            self.process.terminate()
            await self.process.wait()
            self.process = None
            self.status = "stopped"
            
    async def restart(self):
        await self.stop()
        await self.start()
        
    def is_running(self):
        return self.process is not None and self.process.returncode is None

browser_manager = BrowserManager()

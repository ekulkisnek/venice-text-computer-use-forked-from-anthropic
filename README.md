# Issues I faced in reorganizing this to be all text based: 

    Firefox Integration Issues:

    Problems with Firefox startup wizard appearing and interrupting automation
    Need for specific handling of Firefox startup with flags like --kiosk and --no-remote
    Special instructions needed for URL entry and navigation

    PDF Handling Complications:

    Initial attempts to read PDFs through screenshots were inefficient
    Had to pivot to a different approach using curl to download PDFs
    Required additional tools (pdftotext) for proper PDF content extraction

    DOM Interface Testing:

    Multiple test failures visible in the logs for DOM interface tests
    Issues with query builder implementation as seen in test_dom_interface.py
    Integration test complexities between DOM elements and content extraction

    Content Extraction Challenges:

    Had to handle different types of content (text, PDFs, HTML) with different strategies
    Required multiple extraction tools and approaches
    Complex integration between DOM elements and content processors

    Display/X Server Setup:

    Required specific configuration with Xvfb for headless operation
    Needed careful process management (killing existing processes)
    Display configuration dependencies between X server and window manager

    Asynchronous Operation:

    Complexity in handling async operations in Streamlit
    Message handling and state management challenges
    Tool output and API response callback coordination

The project seems to have evolved from simpler approaches to more robust solutions, particularly around content extraction and browser automation.


# Old readme
# Anthropic Computer Use Demo on Replit

## Getting started
* Add your ANTHROPIC_API_KEY to the Secrets pane
* Click Run
* Watch the AI work in the Output pane
* Send commands to it in the Webview

## Caution

Computer use is a beta feature. Please be aware that computer use poses unique risks that are distinct from standard API features or chat interfaces. These risks are heightened when using computer use to interact with the internet. To minimize risks, consider taking precautions such as:

* Use a dedicated virtual machine or container with minimal privileges to prevent direct system attacks or accidents. (Covered by using Replit)
* Avoid giving the model access to sensitive data, such as account login information, to prevent information theft.
* Limit internet access to an allowlist of domains to reduce exposure to malicious content.
* Ask a human to confirm decisions that may result in meaningful real-world consequences as well as any tasks requiring affirmative consent, such as accepting cookies, executing financial transactions, or agreeing to terms of service.
* In some circumstances, Claude will follow commands found in content even if it conflicts with the user's instructions. For example, instructions on webpages or contained in images may override user instructions or cause Claude to make mistakes. We suggest taking precautions to isolate Claude from sensitive data and actions to avoid risks related to prompt injection.

Finally, please inform end users of relevant risks and obtain their consent prior to enabling computer use in your own products.

## Credits
Based on https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo
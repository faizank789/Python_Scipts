// Set the number of milliseconds to wait between tab switches
const interval = 10 * 1000;

// Get the current active tab
chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
  // Get the current tab's index
  const currentTabIndex = tabs[0].index;

  // Switch to the next tab every 10 seconds
  setInterval(function() {
    // Get all tabs in the current window
    chrome.tabs.query({currentWindow: true}, function(tabs) {
      // Calculate the next tab's index
      let nextTabIndex = (currentTabIndex + 1) % tabs.length;

      // Switch to the next tab
      chrome.tabs.update(tabs[nextTabIndex].id, {active: true});

      // Update the current tab's index
      currentTabIndex = nextTabIndex;
    });
  }, interval);
});

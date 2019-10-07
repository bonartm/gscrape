()=>{
    Object.definePropertery(navigator, 'webdriver', {
        get: () => false,
    });

    Object.defineProperty(navigator, 'plugins', {
        get: () => [1, 2, 3, 4, 5],
    });

    Object.defineProperty(navigator, 'languages', {
        get: () => ['en-US', 'en'],
    });


    window.navigator.chrome = {
        runtime: {},
        // etc.
    };

    //window.navigator = {};

    const originalQuery = window.navigator.permissions.query;
    return window.navigator.permissions.query = (parameters) => (
      parameters.name === 'notifications' ?
        Promise.resolve({ state: Notification.permission }) :
        originalQuery(parameters)
    );        
}
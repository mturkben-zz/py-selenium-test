var { By, Builder } = require('selenium-webdriver');
var chrome = require('selenium-webdriver/chrome');
var path = require('chromedriver').path;

var service = new chrome.ServiceBuilder(path).build();
chrome.setDefaultService(service);

(async function example() {
    let driver = await new Builder().forBrowser('chrome').build();


    await driver.get('https://www.instagram.com/accounts/login/');
    setTimeout(async() => {
        await driver.findElement(By.css('[name="username"]')).sendKeys("mturkben721@gmail.com");
        await driver.findElement(By.css('[name="password"]')).sendKeys("ryzer346mmt.M");
        await driver.findElement(By.css('[type="submit"]')).click();
    }, 2000)
})();
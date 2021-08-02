const puppeteer = require("puppeteer");
var mysql = require('mysql');

async function boring(){
    const browser = await puppeteer.launch({
        headless: false
    })
    let page = browser.newPage();
    await page.goto("")
}

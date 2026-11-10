const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport:{width:900,height:1200}});
  await p.goto('file://' + __dirname + '/notes.html');
  await p.evaluate(() => window.handify());
  await p.waitForSelector('body[data-ready="1"]');
  console.log(JSON.stringify(await p.evaluate(() => window.__report)));
  if (process.argv[2] === 'png') {
    const pages = await p.$$('.page');
    for (let i = 0; i < pages.length; i++) await pages[i].screenshot({path: __dirname + `/prev/p${i+1}.png`});
  }
  await p.emulateMedia({media:'print'});
  await p.pdf({path: __dirname + '/out.pdf', width:'794px', height:'1123px', printBackground:true, margin:{top:0,bottom:0,left:0,right:0}});
  await b.close();
})();

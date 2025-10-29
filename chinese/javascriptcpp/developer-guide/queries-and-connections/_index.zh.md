---
title: 使用JavaScript通过C++管理查询和连接
linktitle: 查询和连接
type: docs
weight: 700
url: /zh/javascript-cpp/managing-database-connections/
description: 学习如何使用JavaScript通过C++结合Aspose.Cells管理数据库连接和执行查询。
keywords: 管理数据库连接JavaScript通过C++，执行查询JavaScript通过C++，数据库交互JavaScript通过C++
---

## **介绍**
管理数据库连接和执行查询是需要与结构化数据交互的应用程序的基础，尤其是在处理Excel文件和数据库时。Aspose.Cells for JavaScript通过C++提供了完整的功能以高效完成这些任务。

## **连接到数据库**
要连接到数据库，您可以使用与您的数据库类型相关的连接字符串。以下是使用JavaScript与C++集成建立连接的示例。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - SQLite Connect Conversion</title>
    </head>
    <body>
        <h1>SQLite Connect Example (Browser Simulation)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <br/><br/>
        <input type="text" id="dbPath" placeholder="path_to_your_database.db" style="width:300px;" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        // Simulated createConnection for browser environment
        // (JavaScript `require('node-sqlite')` cannot be used in browser)
        function createConnection(databasePath) {
            return {
                databasePath,
                connect(callback) {
                    // Simulate async connection attempt
                    setTimeout(() => {
                        if (!databasePath || databasePath.toLowerCase().includes('error') || databasePath.toLowerCase().includes('invalid')) {
                            const err = new Error('Failed to connect to database: ' + databasePath);
                            callback(err);
                        } else {
                            callback(null);
                        }
                    }, 300);
                }
            };
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const dbPathInput = document.getElementById('dbPath').value || 'path_to_your_database.db';

            // Convert JavaScript pattern:
            // const { createConnection } = require('node-sqlite');
            // const db = createConnection('path_to_your_database.db');
            //
            // db.connect(err => { ... });
            //
            // to browser-compatible simulation:

            const db = createConnection(dbPathInput);

            db.connect(err => {
                if (err) {
                    console.error('Error connecting to the database:', err);
                    document.getElementById('result').innerHTML = `<p style="color: red;">Error connecting to the database: ${err.message}</p>`;
                    return;
                }
                console.log('Connected to the database successfully!');
                document.getElementById('result').innerHTML = '<p style="color: green;">Connected to the database successfully!</p>';
            });
        });
    </script>
</html>
```

## **执行查询**
连接成功后，可以对数据库执行查询。以下是执行简单SQL查询以检索数据的示例。

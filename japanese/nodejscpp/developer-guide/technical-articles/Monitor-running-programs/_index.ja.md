---  
title: Node.js（C++経由）による実行中プログラムの監視  
linktitle: 実行中のプログラムの監視  
type: docs  
weight: 20  
url: /ja/nodejs-cpp/monitor-running-programs/  
---  

## **実行中のプログラムの監視方法**

以下のサンプルコードは、実行中のプログラムを監視する方法を示しています。このコードは、[Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/)に関するコードの実行監視に使用できます。単純に [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/) クラスを使って監視オブジェクトを作成し、 [LoadOptions.setInterruptMonitor(AbstractInterruptMonitor)] 関数で実行パラメータに追加し、[startMonitor](https://reference.aspose.com/cells/nodejs-cpp/systemtimeinterruptmonitor/#startMonitor-number-) 関数で期待される中断時間（ミリ秒）を設定します。監視コードの実行時間が想定時間を超えると、プログラムは中断され例外がスローされます。

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Large.xlsx");

const monitor = new AsposeCells.SystemTimeInterruptMonitor(false);
const lopts = new AsposeCells.LoadOptions();
lopts.setInterruptMonitor(monitor);
monitor.startMonitor(1000); // time limit is 1 second

// Loads the workbook with the specified load options
const wb = new AsposeCells.Workbook(filePath, lopts);
// if the time cost of loading the template file exceeds one second, interruption will be required and exception will be thrown here
// otherwise starts to monitor the save procedure
monitor.startMonitor(1500); // time limit is 1.5 seconds
wb.save("result.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}

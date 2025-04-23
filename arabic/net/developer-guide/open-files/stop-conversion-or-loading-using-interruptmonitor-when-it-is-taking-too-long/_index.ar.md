---
title: توقّف عن التحويل أو التحميل باستخدام InterruptMonitor عندما يستغرق وقتًا طويلاً
type: docs
weight: 100
url: /ar/net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **سيناريوهات الاستخدام المحتملة**

Aspose.Cells يسمح لك بإيقاف تحويل جدول العمل إلى تنسيقات مختلفة مثل PDF، HTML وما إلى ذلك باستخدام كائن [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) عندما يستغرق الأمر وقتًا طويلاً. يكون عملية التحويل مكثفة للكمبيوتر والذاكرة ومن المفيد في كثير من الأحيان إيقافها عندما تكون الموارد محدودة. يمكنك استخدام [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) كل من لإيقاف التحويل وكذلك لإيقاف تحميل جدول عمل ضخم. يرجى استخدام خاصية [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/interruptmonitor) لإيقاف التحويل وخاصية [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/interruptmonitor) لتحميل جدول العمل الضخم.

## **توقّف عن التحويل أو التحميل باستخدام InterruptMonitor عندما يستغرق وقتًا طويلاً**

يشرح الكود العينة التالي استخدام كائن [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor). يحول الكود ملف إكسل كبير إلى PDF. سيستغرق عدة ثوانٍ (أي *أكثر من 30 ثانية*) لتحويله بسبب هذه الأسطر من الكود.

{{< highlight csharp >}}

//Access cell J1000000 and add some text inside it.

Cell cell = ws.Cells["J1000000"];

cell.PutValue("This is text.");

{{< /highlight >}}

كما ترون **J1000000** هي خلية بعيدة جدًا في ملف XLSX. ومع ذلك، يقوم طريقة **WaitForWhileAndThenInterrupt()** بإيقاف التحويل بعد 10 ثوانٍ وينتهي/ينقطع البرنامج. يرجى استخدام الكود التالي لتنفيذ الكود العينة.

{{< highlight csharp >}}

 new StopConversionOrLoadingUsingInterruptMonitor().TestRun();

{{< /highlight >}}

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-StopConversionOrLoadingUsingInterruptMonitor.cs" >}}
{{< app/cells/assistant language="csharp" >}}

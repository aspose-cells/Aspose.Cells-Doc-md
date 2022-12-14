---
title: أوقف التحويل أو التحميل باستخدام InterruptMonitor عندما يستغرق وقتًا طويلاً
type: docs
weight: 100
url: /ar/net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---
## **سيناريوهات الاستخدام الممكنة**

يسمح لك Aspose.Cells بإيقاف تحويل المصنف إلى تنسيقات مختلفة مثل PDF و HTML وما إلى ذلك باستخدام امتداد[**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) كائن عندما يستغرق وقتا طويلا. غالبًا ما تكون عملية التحويل كثيفة الاستخدام لوحدة المعالجة المركزية والذاكرة وغالبًا ما يكون من المفيد إيقافها عندما تكون الموارد محدودة. يمكنك استخدام[**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) سواء لإيقاف التحويل وكذلك لإيقاف تحميل مصنف ضخم. يرجى استخدام[**المصنف**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/interruptmonitor) خاصية وقف التحويل و[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/interruptmonitor) خاصية تحميل مصنف ضخم.

## **أوقف التحويل أو التحميل باستخدام InterruptMonitor عندما يستغرق وقتًا طويلاً**

يشرح نموذج التعليمات البرمجية التالي استخدام[**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) هدف. يقوم الكود بتحويل ملف Excel كبير جدًا إلى PDF. سيستغرق الأمر عدة ثوانٍ (على سبيل المثال*أكثر من 30 ثانية*) لتحويلها بسبب هذه الأسطر من التعليمات البرمجية.

{{< highlight "csharp" >}}

//Access cell J1000000 and add some text inside it.

Cell cell = ws.Cells["J1000000"];

cell.PutValue("This is text.");

{{< /highlight >}}

 كما ترى**J1000000** هي خلية أبعد تمامًا في ملف XLSX. ومع ذلك ، فإن**WaitForWhileAndThenInterrupt ()**الطريقة تقاطع التحويل بعد 10 ثوانٍ وينتهي البرنامج / ينتهي. الرجاء استخدام التعليمات البرمجية التالية لتنفيذ نموذج التعليمات البرمجية.

{{< highlight "csharp" >}}

 new StopConversionOrLoadingUsingInterruptMonitor().TestRun();

{{< /highlight >}}

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-StopConversionOrLoadingUsingInterruptMonitor.cs" >}}

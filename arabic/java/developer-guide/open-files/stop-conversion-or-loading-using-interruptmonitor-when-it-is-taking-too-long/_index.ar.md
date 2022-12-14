---
title: أوقف التحويل أو التحميل باستخدام InterruptMonitor عندما يستغرق وقتًا طويلاً
type: docs
weight: 100
url: /ar/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---
## **سيناريوهات الاستخدام الممكنة**

يسمح لك Aspose.Cells بإيقاف تحويل المصنف إلى تنسيقات مختلفة مثل PDF و HTML وما إلى ذلك باستخدام امتداد[**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)كائن عندما يستغرق وقتا طويلا. غالبًا ما تكون عملية التحويل كثيفة الاستخدام لوحدة المعالجة المركزية والذاكرة وغالبًا ما يكون من المفيد إيقافها عندما تكون الموارد محدودة. يمكنك استخدام[**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)سواء لإيقاف التحويل وكذلك لإيقاف تحميل مصنف ضخم. يرجى استخدام[**المصنف**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#InterruptMonitor)خاصية وقف التحويل و[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#InterruptMonitor)خاصية تحميل مصنف ضخم.

## **أوقف التحويل أو التحميل باستخدام InterruptMonitor عندما يستغرق وقتًا طويلاً**

يشرح نموذج التعليمات البرمجية التالي استخدام[**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)هدف. يقوم الكود بتحويل ملف Excel كبير جدًا إلى PDF. سيستغرق الأمر عدة ثوانٍ (على سبيل المثال*أكثر من 30 ثانية*) لتحويلها بسبب هذه الأسطر من التعليمات البرمجية.

{{< highlight "java" >}}

//Access cell AB1000000 and add some text inside it.

Cell cell = ws.getCells().get("AB1000000");

cell.putValue("This is text.");

{{< /highlight >}}

كما ترى**AB1000000**هي خلية أبعد تمامًا في ملف XLSX. ومع ذلك ، فإن*WaitForWhileAndThenInterrupt ()*الطريقة تقاطع التحويل بعد 10 ثوانٍ وينتهي البرنامج / ينتهي. الرجاء استخدام التعليمات البرمجية التالية لتنفيذ نموذج التعليمات البرمجية.

{{< highlight "java" >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}

---
title: Aspose.Cells for Java و PHP
type: docs
weight: 20
url: /ar/java/aspose-cells-for-java-and-php/
---
{{% alert color="primary" %}} 

 يمكن لمطوري PHP استخدام Aspose.Cells for Java في تطبيقات PHP. للعمل مع Aspose.Cells for Java و PHP ، استخدم PHP الإصدار 5 (المعروف باسم PHP5). يمكن أيضًا استخدام PHP4 للوصول إلى Aspose.Cells for Java ولكنه أكثر تعقيدًا من استخدام PHP5.

{{% /alert %}} 
## **العمل مع PHP**
### **باستخدام PHP5**
 يوفر Aspose.Cells for Java فئات مجمعة PHP5 تسهل على المطورين استخدام مكتبة Aspose.Cells دون العمل مع فئات Java مباشرة.

 يمكن العثور على فئات المجمّع هذه في دليل PHP لأرشيف aspose.cells.zip في شكل ملف PHP.
## **باستخدام PHP4**
 يعمل PHP4 أيضًا مع Aspose.Cells for Java ولكن في هذه الحالة ، سيحتاج المطورون إلى العمل مع فئات Java مباشرةً.

{{% alert color="primary" %}} 

 لا تنس إضافة aspose.cells.jar إلى java.class.path في ملف php.ini.

 توفر فئات المجمّع PHP بعض الطرق الثابتة لإنشاء فئات PHP لفئة Java المقابلة ، في ClassFactory مع التوقيع createXXX (). إذا تم تحميل المُنشئات بشكل زائد ، يتم تعريف جميع الطرق المقابلة في ClassFactory على أنها إنشاء + الرقم التسلسلي + اسم الفئة ، على سبيل المثال: ((createXXX ()}} ، create1XXX (args ...) ، create2XXX (args ...) ، وهلم جرا.

يتم تعريف جميع الثوابت في PHP على أنها ClassName + "" + ConstantName ، على سبيل المثال ، BorderLineType.NONE يتم تعريفها على أنها BorderLineType NONE في PHP.

 إذا تم تحميل الطرق بشكل زائد ، يتم تعريفها على أنها اسم الطريقة + الرقم التسلسلي ، على سبيل المثال cell.setValue ، cell.setValue1 () ، cell.setValue2 () ، وما إلى ذلك.

 يتم تعريف طريقة clone () على أنها cloneObject ().

{{% /alert %}} 

**بي أتش بي**

{{< highlight "csharp" >}}

 <?php

require_once("java/Java.inc");

require("AsposeCells.php");

$workbook = ClassFactory::createWorkbook();

$workbook->open5("t1.xls");

$cell = $workbook->getWorksheets()->get(0)->getCells()->getCell(0, 0);

$cell->setValue6("Hello World!"); 

$workbook->save5("t.xls");

?>



{{< /highlight >}}

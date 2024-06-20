---
title: Aspose.Cells for Java وPHP
type: docs
weight: 20
url: /ar/java/aspose-cells-for-java-and-php/
---

{{% alert color="primary" %}} 

يمكن لمطوري PHP استخدام Aspose.Cells for Java في تطبيقات PHP. للعمل مع Aspose.Cells for Java وPHP، استخدم إصدار PHP 5 (المعروف باسم PHP5). يمكن أيضًا استخدام PHP4 للوصول إلى Aspose.Cells for Java ولكنه أكثر تعقيدًا من استخدام PHP5. 

{{% /alert %}} 
## **العمل مع PHP**
### **استخدام PHP5**
يوفر Aspose.Cells for Java فئات تعليف PHP5 تجعل من السهل على المطورين استخدام مكتبة Aspose.Cells دون العمل مع فئات جافا مباشرة. 

يمكن العثور على هذه الفئات التعليف في دليل PHP لأرشيف aspose.cells.zip على شكل ملف PHP. 
## **استخدام PHP4**
يعمل أيضاً PHP4 مع Aspose.Cells for Java ولكن في هذه الحالة، سيحتاج المطورون إلى العمل مع فئات Java مباشرة. 

{{% alert color="primary" %}} 

لا تنسى إضافة aspose.cells.jar إلى java.class.path في ملف php.ini. 

توفر فئات الغلاف الخاصة بـ PHP بعض الطرق الثابتة لإنشاء فئات PHP للفئة Java المقابلة، في ClassFactory مع توقيع createXXX(). إذا كانت البناءات محملة، يتم تعريف جميع الطرق المقابلة في ClassFactory كـ create+الرقم التسلسلي+اسم الفئة، على سبيل المثال: ((createXXX()}}, create1XXX(args...), create2XXX(args...), وهكذا. 

تم تعريف جميع الثوابت في PHP كـ اسم الفئة+" "+اسم الثابت، على سبيل المثال، تم تعريف BorderLineType.NONE كـ BorderLineType NONE في PHP. 

إذا كانت الطرق محملة، تم تعريفها كـ اسم الطريقة+الرقم التسلسلي، على سبيل المثال cell.setValue، cell.setValue1()، cell.setValue2()، وهكذا. 

تم تعريف طريقة الاستنساخ (clone()) كـ cloneObject(). 

{{% /alert %}} 

**PHP**

{{< highlight csharp >}}

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

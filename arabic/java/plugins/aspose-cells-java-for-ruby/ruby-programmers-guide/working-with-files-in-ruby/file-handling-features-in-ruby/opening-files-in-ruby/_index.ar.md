---
title: فتح الملفات في روبي
type: docs
weight: 10
url: /ar/java/opening-files-in-ruby/
---
## **Aspose.Cells - طرق بسيطة لفتح ملفات Excel**
### **فتح من خلال المسار**
ما عليك سوى فتح ملف Microsoft Excel بالرجوع إلى مسار الملف

**كود روبي**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

{{< /highlight >}}
### **فتح من خلال تيار**
في بعض الأحيان ، يتم تخزين ملف Excel الذي تريد فتحه كتدفق. في هذه الحالة ، استخدم إصدارًا محملاً بشكل زائد من الأسلوب Open الذي يأخذ كائن Stream الذي يحتوي على ملف Excel لفتح الملف.

**كود روبي**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

fstream = IO.sysopen(@data_dir + 'Book1.xls')

workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

{{< /highlight >}}

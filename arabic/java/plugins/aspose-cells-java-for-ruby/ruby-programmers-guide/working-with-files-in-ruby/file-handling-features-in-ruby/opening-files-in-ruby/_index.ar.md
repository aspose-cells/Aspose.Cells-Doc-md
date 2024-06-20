---
title: فتح الملفات في روبي
type: docs
weight: 10
url: /ar/java/opening-files-in-ruby/
---

## **Aspose.Cells - طرق بسيطة لفتح ملفات إكسل**
### **الفتح عبر المسار**
فقط قم بفتح ملف Microsoft Excel عن طريق الإشارة إلى مسار الملف

**كود Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

{{< /highlight >}}
### **الفتح عبر التيار**
في بعض الأحيان، يتم تخزين ملف إكسل الذي ترغب في فتحه كتيار. في هذه الحالة، استخدم الإصدار المحمل من طريقة الفتح التي تأخذ كائن التيار الذي يحتوي على ملف إكسل لفتح الملف.

**كود Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

fstream = IO.sysopen(@data_dir + 'Book1.xls')

workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

{{< /highlight >}}

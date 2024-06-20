---
title: إدارة خصائص المستند في روبي
type: docs
weight: 90
url: /ar/java/managing-document-properties-in-ruby/
---

## **Aspose.Cells - الوصول إلى خصائص المستند**
يمكن للمطورين استخدام ** Index ** أو ** Name ** للخاصية للحصول على خاصية معينة من مجموعة ** custom_properties ** كما هو موضح أدناه في المثال.

**كود Ruby**

{{< highlight ruby >}}

 def get_properties()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Retrieve a list of all custom document properties of the Excel file

    custom_properties = workbook.getWorksheets().getCustomDocumentProperties()

    # Accessng a custom document property by using the property index

    puts "Property By Index: " +  custom_properties.get(1).to_string

    # Accessng a custom document property by using the property name

    puts "Property By Name: " + custom_properties.get("Publisher").to_string

end

{{< /highlight >}}
## **Aspose.Cells - إضافة خصائص مخصصة**
لإضافة خصائص المستند المخصصة باستخدام Aspose.Cells Java لـ Ruby ، اتصل بطريقة ** add_custom_property ** في وحدة ** Document **.

**كود Ruby**

{{< highlight ruby >}}

 def add_custom_property()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Retrieve a list of all custom document properties of the Excel file

    custom_properties = workbook.getWorksheets().getCustomDocumentProperties()

    # Adding a custom document property to the Excel file

    custom_properties.add("Publisher", "Aspose")

    # Save the document in PDF format

    workbook.save(data_dir + "Add_Property.xls")

    puts "Added custom property successfully."

end   

{{< /highlight >}}
## **Aspose.Cells - إزالة الخصائص المخصصة**
لإزالة خصائص المستند المخصصة باستخدام Aspose.Cells Java لـ Ruby ، اتصل بطريقة ** remove_custom_property ** في وحدة ** Document **.

**كود Ruby**

{{< highlight ruby >}}

 def remove_custom_property()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Retrieve a list of all custom document properties of the Excel file

    custom_properties = workbook.getWorksheets().getCustomDocumentProperties()

    # Adding a custom document property to the Excel file

    custom_properties.remove("Publisher")

    # Save the document in PDF format

    workbook.save(data_dir + "Removed_Property.xls")

    puts "Removed custom property successfully."

end   

{{< /highlight >}}
## **تحميل رمز التشغيل**
قم بتنزيل **الوصول إلى خصائص الوثيقة (Aspose.Cells)** من أي من المواقع المشفرة المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/document.rb)

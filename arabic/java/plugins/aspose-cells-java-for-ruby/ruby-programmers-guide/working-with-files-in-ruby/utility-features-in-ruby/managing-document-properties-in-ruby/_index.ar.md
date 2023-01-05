---
title: إدارة خصائص الوثيقة في روبي
type: docs
weight: 90
url: /ar/java/managing-document-properties-in-ruby/
---
## **Aspose.Cells - الوصول إلى خصائص الوثيقة**
يمكن للمطورين الاستفادة من**فِهرِس**أو**اسم** من العقار للحصول على عقار معين من أ**خصائص_مخصصة**المجموعة كما هو موضح أدناه في المثال.

**كود روبي**

{{< highlight "ruby" >}}

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
لإضافة خصائص وثيقة مخصصة باستخدام Aspose.Cells Java لروبي ، اتصل**add_custom_property** طريقة**وثيقة** وحدة.

**كود روبي**

{{< highlight "ruby" >}}

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
## **Aspose.Cells - إزالة الخصائص المهيأة**
 لإزالة خصائص المستند المخصصة باستخدام Aspose.Cells Java لروبي ، اتصل**remove_custom_property** طريقة**وثيقة** وحدة.

**كود روبي**

{{< highlight "ruby" >}}

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
## **قم بتنزيل كود التشغيل**
 تحميل**الوصول إلى خصائص المستند (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/document.rb)

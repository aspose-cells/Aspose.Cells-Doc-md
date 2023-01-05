---
title: Yuvalanmış Nesneleri Kullanma
type: docs
weight: 50
url: /tr/net/using-nested-objects/
---
Aspose.Cells, akıllı işaretleyicilerdeki iç içe nesneleri destekler, iç içe nesneler basit olmalıdır.**Bireysel** Aşağıdaki kod için sınıfın kullanıcı tarafından tanımlanması gerekir.

Basit bir şablon dosyası kullanıyoruz. Bazı iç içe akıllı işaretçileri içeren tasarımcı elektronik tablosuna bakın.

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Using Nested Object.xlsx";

//Initialize WorkbookDesigner object

WorkbookDesigner designer = new WorkbookDesigner();

//Load the template file

designer.Workbook = new Workbook(FileName);

//Instantiate the List based on the class

System.Collections.Generic.ICollection<Individual> list = new System.Collections.Generic.List<Individual>();

//Create an object for the Individual class

Individual p1 = new Individual("Damian", 30);

//Create the relevant Wife class for the Individual

p1.Wife = new Wife("Dalya", 28);

//Create another object for the Individual class

Individual p2 = new Individual("Mack", 31);

//Create the relevant Wife class for the Individual

p2.Wife = new Wife("Maaria", 29);

//Add the objects to the list

list.Add(p1);

list.Add(p2);

//Specify the DataSource

designer.SetDataSource("Individual", list);

//Process the markers

designer.Process(false);

//Save the Excel file.

designer.Workbook.Save(FileName);


{{< /highlight >}}
## **Örnek Kodu İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Using%20Nested%20Object%20%28Aspose.Cells%29.zip)

---
title: xlsx4j'de Emsalleri ve Bağımlıları İzleme
type: docs
weight: 70
url: /tr/java/tracing-precedents-and-dependents-in-xlsx4j/
---
## **Aspose.Cells - Emsallerin ve Bağımlıların İzlenmesi**
Karmaşık finansal çalışma sayfaları, özellikle işbirliği içinde geliştirilenler, en utanç verici hataları gizleyebilir. Formüllerin doğruluğunu kontrol etmek ve bir hatanın kaynağını bulmak, formül emsal hücreler ve bağımlı hücreler kullandığında zor olabilir.

- **emsal hücreler**başka bir Cell'deki bir formülle başvurulan hücrelerdir. Örneğin, D10 hücresi =B5 formülünü içeriyorsa, B5 hücresi D10 hücresinin emsalidir.
- **Bağımlı hücreler**diğer hücrelere başvuran formüller içerir. Örneğin, D10 hücresi =B5 formülünü içeriyorsa, D10 hücresi B5 hücresinin bağımlısıdır.

Elektronik tablonun okunmasını kolaylaştırmak için, formülde elektronik tablodaki hangi hücrelerin kullanıldığını açıkça göstermek isteyebilirsiniz. Benzer şekilde, diğer hücrelerin bağımlı hücrelerini çıkarmak isteyebilirsiniz.

Aspose.Cells, hücreleri izlemenizi ve hangilerinin bağlantılı olduğunu bulmanızı sağlar.

Emsallerin İzini Sürmek

**Java**

{{< highlight "java" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook(dataDir + "workbook.xls");

Cells cells = workbook.getWorksheets().get(0).getCells();

Cell cell = cells.get("A12");

//Tracing precedents of the cell A12.

//The return array contains ranges and cells.

ReferredAreaCollection ret = cell.getPrecedents();

//Printing all the precedent cells' name.

if(ret != null)

{

  for(int m = 0 ; m < ret.getCount(); m++)

  {

    ReferredArea area = ret.get(m);

    StringBuilder stringBuilder = new StringBuilder();

    if (area.isExternalLink())

    {

        stringBuilder.append("[");

        stringBuilder.append(area.getExternalFileName());

        stringBuilder.append("]");

     }

     stringBuilder.append(area.getSheetName());

     stringBuilder.append("!");

     stringBuilder.append(CellsHelper.cellIndexToName(area.getStartRow(), area.getStartColumn()));

     if (area.isArea())

      {

          stringBuilder.append(":");

          stringBuilder.append(CellsHelper.cellIndexToName(area.getEndRow(), area.getEndColumn()));

      }

      System.out.println("Tracing Precedents: " + stringBuilder.toString());

   }

}

{{< /highlight >}}

Bağımlıları İzleme

**Java**

{{< highlight "java" >}}

 //A1 hücresini al

Cell c = cell.get("A5");

// A5 hücresinin tüm Bağımlılarını al

Cell[]bağımlılar = c.getDependents(true);

için (int ben = 0; ben< dependents.length; i++)

{

     System.out.println("Tracing Dependents: " + dependents[i].getWorksheet().getName() +dependents[i].getName() + ":" + dependents[i].getIntValue());

}

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/tracingprecedentsanddependents/AsposeTracingPrecedentsAndDependents.java)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Emsallerin ve Bağımlıların İzlenmesi](/java/tracing-precedents-and-dependents).

{{% /alert %}}

---
title: Çalışsayfalar Arasında Şekiller Kopyalama
linktitle: Şekilleri Kopyalama
type: docs
weight: 200
url: /tr/net/copy-shapes-between-worksheets/
---

{{% alert color="primary" %}}

Bazı durumlarda, örneğin resimler, grafikler ve diğer çizim nesneleri gibi çalışsayfasındaki unsurları başka çalışsayfalara kopyalamanız gerekebilir. Aspose.Cells bu özelliği destekler. Grafikler, resimler ve diğer nesneler en yüksek hassasiyetle kopyalanabilir.

Bu makale, çalışsayfalar arasında şekillerin nasıl kopyalanacağı konusunda size detaylı bir anlayış sağlar.

{{% /alert %}}

## **Bir Resmi Bir Çalışsayfasından Başka Birine Kopyalama**

Bir resmi bir çalışsayfasından diğerine kopyalamak için aşağıdaki örnek kodda gösterildiği gibi [**Worksheet.Pictures.Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) yöntemini kullanın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyPictureBetweenWorksheets.cs" >}}

## **Bir Grafik Bir Çalışsayfasından Diğerine Kopyalama**

Aşağıdaki kod, bir çalışsayfasından diğerine bir grafik kopyalamak için [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy) yönteminin kullanımını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyChartBetweenWorksheets.cs" >}}

## **Denetimleri ve Diğer Çizim Nesnelerini Bir Çalışsayfasından Diğerine Kopyalama**

Denetimleri ve diğer çizim nesnelerini kopyalamak için örnekte gösterildiği gibi [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy) yöntemini kullanın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyControlsAndOtherDrawingObjects.cs" >}}

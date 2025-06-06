---
title: Çalışsayfalar Arasında Şekiller Kopyalama
linktitle: Şekilleri Kopyalama
type: docs
weight: 200
url: /tr/python-net/copy-shapes-between-worksheets/
description: Bu makale, Aspose.Cells for Python via .NET API aracılığıyla çalışma sayfaları arasında şekil kopyalama işlemini gösterir.
keywords: Python Excel Kütüphanesi, Worksheet ler arasında Şekil Kopyalama, Bir Çizimi Bir Çalışma Sayfasından Diğerine Nasıl Kopyalanır, Bir Grafik Nasıl Kopyalanır, Kontroller ve Diğer Çizim Öğeleri Nasıl Kopyalanır gibi konuları içerir.
---

{{% alert color="primary" %}}

Bazen, bir çalışma sayfasındaki öğeleri, örneğin resimler, grafikler ve diğer çizim nesnelerini, çalışma sayfaları arasında kopyalamanız gerekebilir. Aspose.Cells for Python via .NET bu özelliği destekler. Grafikler, görüntüler ve diğer nesneler en yüksek hassasiyetle kopyalanabilir.

Bu makale, çalışsayfalar arasında şekillerin nasıl kopyalanacağı konusunda size detaylı bir anlayış sağlar.

{{% /alert %}}

## **Bir Resmi Bir Çalışsayfasından Başka Birine Kopyalama**

Bir resmi bir çalışsayfasından diğerine kopyalamak için aşağıdaki örnek kodda gösterildiği gibi [**Worksheet.pictures.add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add/#int-int-io.RawIOBase-int-int) yöntemini kullanın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyPictureBetweenWorksheets.py" >}}

## **Bir Grafik Bir Çalışsayfasından Diğerine Kopyalama**

Aşağıdaki kod, bir çalışsayfasından diğerine bir grafik kopyalamak için [**Worksheet.shapes.add_copy**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_copy/#aspose.cells.drawing.Shape-int-int-int-int) yönteminin kullanımını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyChartBetweenWorksheets.py" >}}

## **Denetimleri ve Diğer Çizim Nesnelerini Bir Çalışsayfasından Diğerine Kopyalama**

Denetimleri ve diğer çizim nesnelerini kopyalamak için örnekte gösterildiği gibi [**Worksheet.shapes.add_copy**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_copy/#aspose.cells.drawing.Shape-int-int-int-int) yöntemini kullanın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyControlsAndOtherDrawingObjects.py" >}}

---
title: Отрисовка сплошной сетки при преобразовании Excel в PDF
type: docs
weight: 380
url: /ru/java/render-solid-gridline-while-converting-excel-to-pdf/

---

Для совместимости со старыми версиями, Aspose.Cells по умолчанию рендерит линию сетки пунктирной при конвертации Excel в PDF. Однако современные версии Excel отображают линию сетки сплошной.

Опция [PdfSaveOptions.GridlineTypes](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setGridlineType-int-) позволяет Aspose.Cells также отображать линию сетки как сплошную. 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-SolidGridlineInPdf.java" >}}

![solid-gridline.png](solid-gridline.png)

{{< app/cells/assistant language="java" >}}

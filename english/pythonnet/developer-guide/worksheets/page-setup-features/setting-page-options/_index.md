---
title: Setting Page Options
type: docs
weight: 10
url: /python-net/setting-page-options/
description: This article provides sample code to set page options of Excel worksheets programmatically using Aspose.Cells for Python via .NET API. You will be able to set Page Orientation, Scaling Factor, FitToPages Options, Paper Size, Print Quality, First Page Number.
keywords: Python Excel Library, Python set excel page orientation, set excel scaling factor using Python, set excel worksheets paper size in Python, Python How to Set Page Orientation, Python How to Set Scaling Factor, Python How to Set FitToPages Options, Python How to Set Paper Size, Python How to Set Print Quality, Python How to Set First Page Number.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, it is necessary to configure page setup settings for worksheets to control printing. These page setup settings offer various options.

{{% /alert %}}

## **How to Set Page Options**

Page setup options are fully supported in Aspose.Cells for Python via .NET. This article explains how to set page options with Aspose.Cells for Python via .NET and shows code samples for setting:

Aspose.Cells for Python via .NET provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class.

The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides the [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) property that is used to set the page setup options of the worksheet. In fact, this [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) property is an object of the [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) class used to set different page layout options for a printed worksheet. The [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) class provides various properties used to set page setup options. Some of these properties are discussed below.

## **How to Set Page Orientation**

Page orientation can be set to portrait or landscape using the [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) class's [**orientation**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/orientation) property. The [**orientation**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/orientation) property accepts one of the predefined values in the [**PageOrientationType**](https://reference.aspose.com/cells/python-net/aspose.cells/pageorientationtype) enumeration, listed below.

| **Page Orientation Types** | **Description** |
| :- | :- |
| LANDSCAPE | Landscape orientation |
| PORTRAIT | Portrait orientation |

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-PageOrientation-1.py" >}}

## **How to Set Scaling Factor**

It is possible to reduce or enlarge a worksheet's size by adjusting the scaling factor with the [**PageSetup.zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/zoom) property.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-ScalingFactor-1.py" >}}

## **How to Set FitToPages Options**

To fit the contents of the worksheet to a specific number of pages, use the [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) class's [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall/) and [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide/) properties. These properties are also used to scale worksheets.

{{% alert color="primary" %}}

You can either choose the [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall/) and [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide/) or the [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/zoom) property, but not both at the same time.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-FitToPagesOptions-1.py" >}}

## **How to Set Paper Size**

Set the paper size that the worksheets will be printed on using the [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) class's [**paper_size**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_size/) property. The [**paper_size**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_size/) property accepts one of the predefined values in the [**PaperSizeType**](https://reference.aspose.com/cells/python-net/aspose.cells/papersizetype/) enumeration, listed below.

| **Paper Size Types** | **Description** |
| :- | :- |
| PaperLetter | Letter (8‑1/2 in. × 11 in.) |
| PaperLetterSmall | Letter Small (8‑1/2 in. × 11 in.) |
| PaperTabloid | Tabloid (11 in. × 17 in.) |
| PaperLedger | Ledger (17 in. × 11 in.) |
| PaperLegal | Legal (8‑1/2 in. × 14 in.) |
| PaperStatement | Statement (5‑1/2 in. × 8‑1/2 in.) |
| PaperExecutive | Executive (7‑1/4 in. × 10‑1/2 in.) |
| PaperA3 | A3 (297 mm × 420 mm) |
| PaperA4 | A4 (210 mm × 297 mm) |
| PaperA4Small | A4 Small (210 mm × 297 mm) |
| PaperA5 | A5 (148 mm × 210 mm) |
| PaperB4 | JIS B4 (257 mm × 364 mm) |
| PaperB5 | JIS B5 (182 mm × 257 mm) |
| PaperFolio | Folio (8‑1/2 in. × 13 in.) |
| PaperQuarto | Quarto (215 mm × 275 mm) |
| Paper10x14 | 10 in. × 14 in. |
| Paper11x17 | 11 in. × 17 in. |
| PaperNote | Note (8‑1/2 in. × 11 in.) |
| PaperEnvelope9 | Envelope #9 (3‑7/8 in. × 8‑7/8 in.) |
| PaperEnvelope10 | Envelope #10 (4‑1/8 in. × 9‑1/2 in.) |
| PaperEnvelope11 | Envelope #11 (4‑1/2 in. × 10‑3/8 in.) |
| PaperEnvelope12 | Envelope #12 (4‑1/2 in. × 11 in.) |
| PaperEnvelope14 | Envelope #14 (5 in. × 11‑1/2 in.) |
| PaperCSheet | C size sheet |
| PaperDSheet | D size sheet |
| PaperESheet | E size sheet |
| PaperEnvelopeDL | Envelope DL (110 mm × 220 mm) |
| PaperEnvelopeC5 | Envelope C5 (162 mm × 229 mm) |
| PaperEnvelopeC3 | Envelope C3 (324 mm × 458 mm) |
| PaperEnvelopeC4 | Envelope C4 (229 mm × 324 mm) |
| PaperEnvelopeC6 | Envelope C6 (114 mm × 162 mm) |
| PaperEnvelopeC65 | Envelope C65 (114 mm × 229 mm) |
| PaperEnvelopeB4 | Envelope B4 (250 mm × 353 mm) |
| PaperEnvelopeB5 | Envelope B5 (176 mm × 250 mm) |
| PaperEnvelopeB6 | Envelope B6 (176 mm × 125 mm) |
| PaperEnvelopeItaly | Envelope Italy (110 mm × 230 mm) |
| PaperEnvelopeMonarch | Envelope Monarch (3‑7/8 in. × 7‑1/2 in.) |
| PaperEnvelopePersonal | Envelope (3‑5/8 in. × 6‑1/2 in.) |
| PaperFanfoldUS | U.S. Standard Fanfold (14‑7/8 in. × 11 in.) |
| PaperFanfoldStdGerman | German Standard Fanfold (8‑1/2 in. × 12 in.) |
| PaperFanfoldLegalGerman | German Legal Fanfold (8‑1/2 in. × 13 in.) |
| PaperISOB4 | B4 (ISO) 250 × 353 mm |
| PaperJapanesePostcard | Japanese Postcard (100 mm × 148 mm) |
| Paper9x11 | 9 in. × 11 in. |
| Paper10x11 | 10 in. × 11 in. |
| Paper15x11 | 15 in. × 11 in. |
| PaperEnvelopeInvite | Envelope Invite (220 mm × 220 mm) |
| PaperLetterExtra | US Letter Extra 9 ¾ × 12 in |
| PaperLegalExtra | US Legal Extra 9 ¾ × 15 in |
| PaperTabloidExtra | US Tabloid Extra 11.69 × 18 in |
| PaperA4Extra | A4 Extra 9.27 × 12.69 in |
| PaperLetterTransverse | Letter Transverse 8 ¾ × 11 in |
| PaperA4Transverse | A4 Transverse 210 × 297 mm |
| PaperLetterExtraTransverse | Letter Extra Transverse 9 ¾ × 12 in |
| PaperSuperA | SuperA/SuperA/A4 227 × 356 mm |
| PaperSuperB | SuperB/SuperB/A3 305 × 487 mm |
| PaperLetterPlus | US Letter Plus 8.5 × 12.69 in |
| PaperA4Plus | A4 Plus 210 × 330 mm |
| PaperA5Transverse | A5 Transverse 148 × 210 mm |
| PaperJISB5Transverse | B5 (JIS) Transverse 182 × 257 mm |
| PaperA3Extra | A3 Extra 322 × 445 mm |
| PaperA5Extra | A5 Extra 174 × 235 mm |
| PaperISOB5Extra | B5 (ISO) Extra 201 × 276 mm |
| PaperA2 | A2 420 × 594 mm |
| PaperA3Transverse | A3 Transverse 297 × 420 mm |
| PaperA3ExtraTransverse | A3 Extra Transverse 322 × 445 mm |
| PaperJapaneseDoublePostcard | Japanese Double Postcard 200 × 148 mm |
| PaperA6 | A6 105 × 148 mm |
| PaperJapaneseEnvelopeKaku2 | Japanese Envelope Kaku #2 |
| PaperJapaneseEnvelopeKaku3 | Japanese Envelope Kaku #3 |
| PaperJapaneseEnvelopeChou3 | Japanese Envelope Chou #3 |
| PaperJapaneseEnvelopeChou4 | Japanese Envelope Chou #4 |
| PaperLetterRotated | 11 in × 8.5 in |
| PaperA3Rotated | 420 mm × 297 mm |
| PaperA4Rotated | 297 mm × 210 mm |
| PaperA5Rotated | 210 mm × 148 mm |
| PaperJISB4Rotated | B4 (JIS) Rotated 364 × 257 mm |
| PaperJISB5Rotated | B5 (JIS) Rotated 257 × 182 mm |
| PaperJapanesePostcardRotated | Japanese Postcard Rotated 148 × 100 mm |
| PaperJapaneseDoublePostcardRotated | Double Japanese Postcard Rotated 148 × 200 mm |
| PaperA6Rotated | A6 Rotated 148 × 105 mm |
| PaperJapaneseEnvelopeKaku2Rotated | Japanese Envelope Kaku #2 Rotated |
| PaperJapaneseEnvelopeKaku3Rotated | Japanese Envelope Kaku #3 Rotated |
| PaperJapaneseEnvelopeChou3Rotated | Japanese Envelope Chou #3 Rotated |
| PaperJapaneseEnvelopeChou4Rotated | Japanese Envelope Chou #4 Rotated |
| PaperJISB6 | B6 (JIS) 128 × 182 mm |
| PaperJISB6Rotated | B6 (JIS) Rotated 182 × 128 mm |
| Paper12x11 | 12 × 11 in |
| PaperJapaneseEnvelopeYou4 | Japanese Envelope You #4 |
| PaperJapaneseEnvelopeYou4Rotated | Japanese Envelope You #4 Rotated |
| PaperPRC16K | PRC 16K 146 × 215 mm |
| PaperPRC32K | PRC 32K 97 × 151 mm |
| PaperPRCBig32K | PRC 32K (Big) 97 × 151 mm |
| PaperPRCEnvelope1 | PRC Envelope #1 102 × 165 mm |
| PaperPRCEnvelope2 | PRC Envelope #2 102 × 176 mm |
| PaperPRCEnvelope3 | PRC Envelope #3 125 × 176 mm |
| PaperPRCEnvelope4 | PRC Envelope #4 110 × 208 mm |
| PaperPRCEnvelope5 | PRC Envelope #5 110 × 220 mm |
| PaperPRCEnvelope6 | PRC Envelope #6 120 × 230 mm |
| PaperPRCEnvelope7 | PRC Envelope #7 160 × 230 mm |
| PaperPRCEnvelope8 | PRC Envelope #8 120 × 309 mm |
| PaperPRCEnvelope9 | PRC Envelope #9 229 × 324 mm |
| PaperPRCEnvelope10 | PRC Envelope #10 324 × 458 mm |
| PaperPRC16KRotated | PRC 16K Rotated |
| PaperPRC32KRotated | PRC 32K Rotated |
| PaperPRCBig32KRotated | PRC 32K (Big) Rotated |
| PaperPRCEnvelope1Rotated | PRC Envelope #1 Rotated 165 × 102 mm |
| PaperPRCEnvelope2Rotated | PRC Envelope #2 Rotated 176 × 102 mm |
| PaperPRCEnvelope3Rotated | PRC Envelope #3 Rotated 176 × 125 mm |
| PaperPRCEnvelope4Rotated | PRC Envelope #4 Rotated 208 × 110 mm |
| PaperPRCEnvelope5Rotated | PRC Envelope #5 Rotated 220 × 110 mm |
| PaperPRCEnvelope6Rotated | PRC Envelope #6 Rotated 230 × 120 mm |
| PaperPRCEnvelope7Rotated | PRC Envelope #7 Rotated 230 × 160 mm |
| PaperPRCEnvelope8Rotated | PRC Envelope #8 Rotated 309 × 120 mm |
| PaperPRCEnvelope9Rotated | PRC Envelope #9 Rotated 324 × 229 mm |
| PaperPRCEnvelope10Rotated | PRC Envelope #10 Rotated 458 × 324 mm |
| PaperB3 | usual B3 (13.9 × 19.7 in) |
| PaperBusinessCard | Business Card (90 mm × 55 mm) |
| PaperThermal | Thermal (3 × 11 in) |
| Custom | Represents the custom paper size. |

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-ManagePaperSize-1.py" >}}

## **How to Set Print Quality**

Set the print quality of the worksheets to be printed with the [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/) class's [**print_quality**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_quality/) property. The measuring unit for print quality is Dots Per Inch (DPI).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintQuality-1.py" >}}

## **How to Set First Page Number**

Start the numbering of worksheet pages using the [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) class's [**first_page_number**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/first_page_number/) property. The [**first_page_number**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/first_page_number/) property sets the page number of the first worksheet page, and the subsequent pages are numbered in ascending order.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetFirstPageNumber-1.py" >}}
{{< app/cells/assistant language="python-net" >}}

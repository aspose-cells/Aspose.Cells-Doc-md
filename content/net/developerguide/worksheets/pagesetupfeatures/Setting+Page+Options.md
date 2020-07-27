+++
title = "Setting Page Options" 
description = "" 
weight = 16153 
+++

Aspose.Cells for .NET : Setting Page Options  

# Aspose.Cells for .NET : Setting Page Options


Sometimes, it is necessary to configure page setup settings for worksheets to control printing. These page setup settings offer various options.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Setting Page Options](#SettingPageOptions-SettingPageOptions)
    *   1.1 [Page Orientation](#SettingPageOptions-PageOrientation)
    *   1.2 [Scaling Factor](#SettingPageOptions-ScalingFactor)
    *   1.3 [FitToPages Options](#SettingPageOptions-FitToPagesOptions)
    *   1.4 [Paper Size](#SettingPageOptions-PaperSize)
    *   1.5 [Print Quality](#SettingPageOptions-PrintQuality)
    *   1.6 [First Page Number](#SettingPageOptions-FirstPageNumber)
{{< /panel >}}
 

 

## Setting Page Options

Page setup options are fully supported in Aspose.Cells. This article explains how to set page options with Aspose.Cells and shows code samples for setting:

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook), that represents a Microsoft Excel file. The [Workbook ](https://apireference.aspose.com/net/cells/aspose.cells/workbook)class contains a [Worksheets](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class.

The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class provides the [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/pagesetup) property that is used to set the page setup options of the worksheet. In fact, this [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/pagesetup) property is an object of the [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup) class used to set different page layout options for a printed worksheet. The [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup) class provides various properties used to set page setup options. Some of these properties are discussed below.

### Page Orientation

Page orientation can be set to portrait or landscape using the [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup) class' [Orientation](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/orientation) property. The [Orientation](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/orientation) property accepts one of the pre-defined values in the [PageOrientationType](https://apireference.aspose.com/net/cells/aspose.cells/pageorientationtype) enumeration, listed below.

{{< table style="table-striped" >}}
|Page Orientation Types|Description|
|:----|:----|
|Landscape|Landscape orientation|
|Portrait|Portrait orientation|
{{< /table >}}

### Scaling Factor

It is possible to reduce or enlarge a worksheet's size by adjusting the scaling factor with the [PageSetup.Zoom](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/zoom) property.

### FitToPages Options

To fit the contents of the worksheet to a specific number of pages, use the [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup) class' [FitToPagesTall](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/fittopagestall) and [FitToPagesWide](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/fittopageswide) properties. These properties are also used to scale worksheets.

You can either choose the [FitToPagesTall](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/fittopagestall)/[FitToPagesWide](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/fittopageswide) or the [Zoom](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/zoom) property but not both at the same time.

### Paper Size

Set the paper size that the worksheets will be printed to using the [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup) class' [PaperSize](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/papersize) property. The [PaperSize](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/papersize) property accepts one of the pre-defined values in the [PaperSizeType](https://apireference.aspose.com/net/cells/aspose.cells/papersizetype) enumeration, listed below.

{{< table style="table-striped" >}}
|Paper Size Types|Description|
|:----|:----|
|PaperLetter|Letter (8-1/2 in. x 11 in.)|
|PaperLetterSmall|Letter Small (8-1/2 in. x 11 in.)|
|PaperTabloid|Tabloid (11 in. x 17 in.)|
|PaperLedger|Ledger (17 in. x 11 in.)|
|PaperLegal|Legal (8-1/2 in. x 14 in.)|
|PaperStatement|Statement (5-1/2 in. x 8-1/2 in.)|
|PaperExecutive|Executive (7-1/4 in. x 10-1/2 in.)|
|PaperA3|A3 (297 mm x 420 mm)|
|PaperA4|A4 (210 mm x 297 mm)|
|PaperA4Small|A4 Small (210 mm x 297 mm)|
|PaperA5|A5 (148 mm x 210 mm)|
|PaperB4|JIS B4 (257 mm x 364 mm)|
|PaperB5|JIS B5 (182 mm x 257 mm)|
|PaperFolio|Folio (8-1/2 in. x 13 in.)|
|PaperQuarto|Quarto (215 mm x 275 mm)|
|Paper10x14|10 in. x 14 in.|
|Paper11x17|11 in. x 17 in.|
|PaperNote|Note (8-1/2 in. x 11 in.)|
|PaperEnvelope9|Envelope #9 (3-7/8 in. x 8-7/8 in.)|
|PaperEnvelope10|Envelope #10 (4-1/8 in. x 9-1/2 in.)|
|PaperEnvelope11|Envelope #11 (4-1/2 in. x 10-3/8 in.)|
|PaperEnvelope12|Envelope #12 (4-1/2 in. x 11 in.)|
|PaperEnvelope14|Envelope #14 (5 in. x 11-1/2 in.)|
|PaperCSheet|C size sheet|
|PaperDSheet|D size sheet|
|PaperESheet|E size sheet|
|PaperEnvelopeDL|Envelope DL (110 mm x 220 mm)|
|PaperEnvelopeC5|Envelope C5 (162 mm x 229 mm)|
|PaperEnvelopeC3|Envelope C3 (324 mm x 458 mm)|
|PaperEnvelopeC4|Envelope C4 (229 mm x 324 mm)|
|PaperEnvelopeC6|Envelope C6 (114 mm x 162 mm)|
|PaperEnvelopeC65|Envelope C65 (114 mm x 229 mm)|
|PaperEnvelopeB4|Envelope B4 (250 mm x 353 mm|
|PaperEnvelopeB5|Envelope B5 (176 mm x 250 mm)|
|PaperEnvelopeB6|Envelope B6 (176 mm x 125 mm)|
|PaperEnvelopeItaly|Envelope Italy (110 mm x 230 mm)|
|PaperEnvelopeMonarch|Envelope Monarch (3-7/8 in. x 7-1/2 in.)|
|PaperEnvelopePersonal|Envelope (3-5/8 in. x 6-1/2 in.)|
|PaperFanfoldUS|U.S. Standard Fanfold (14-7/8 in. x 11 in.)|
|PaperFanfoldStdGerman|German Standard Fanfold (8-1/2 in. x 12 in.)|
|PaperFanfoldLegalGerman|German Legal Fanfold (8-1/2 in. x 13 in.)|
|PaperISOB4|B4 (ISO) 250 x 353 mm|
|PaperJapanesePostcard|Japanese Postcard (100mm x 148mm)|
|Paper9x11|9 in. x 11 in.|
|Paper10x11|10 in. x 11 in.|
|Paper15x11|15 in. x 11 in.|
|PaperEnvelopeInvite|Envelope Invite(220mm x 220mm)|
|PaperLetterExtra|US Letter Extra 9 \\275 x 12 in|
|PaperLegalExtra|US Legal Extra 9 \\275 x 15 in|
|PaperTabloidExtra|US Tabloid Extra 11.69 x 18 in|
|PaperA4Extra|A4 Extra 9.27 x 12.69 in|
|PaperLetterTransverse|Letter Transverse 8 \\275 x 11 in|
|PaperA4Transverse|A4 Transverse 210 x 297 mm|
|PaperLetterExtraTransverse|Letter Extra Transverse 9\\275 x 12 in|
|PaperSuperA|SuperA/SuperA/A4 227 x 356 mm|
|PaperSuperB|SuperB/SuperB/A3 305 x 487 mm|
|PaperLetterPlus|US Letter Plus 8.5 x 12.69 in|
|PaperA4Plus|A4 Plus 210 x 330 mm|
|PaperA5Transverse|A5 Transverse 148 x 210 mm|
|PaperJISB5Transverse|B5 (JIS) Transverse 182 x 257 mm|
|PaperA3Extra|A3 Extra 322 x 445 mm|
|PaperA5Extra|A5 Extra 174 x 235 mm|
|PaperISOB5Extra|B5 (ISO) Extra 201 x 276 mm|
|PaperA2|A2 420 x 594 mm|
|PaperA3Transverse|A3 Transverse 297 x 420 mm|
|PaperA3ExtraTransverse|A3 Extra Transverse 322 x 445 mm|
|PaperJapaneseDoublePostcard|Japanese Double Postcard 200 x 148 mm|
|PaperA6|A6 105 x 148 mm|
|PaperJapaneseEnvelopeKaku2|Japanese Envelope Kaku #2|
|PaperJapaneseEnvelopeKaku3|Japanese Envelope Kaku #3|
|PaperJapaneseEnvelopeChou3|Japanese Envelope Chou #3|
|PaperJapaneseEnvelopeChou4|Japanese Envelope Chou #4|
|PaperLetterRotated|11in x 8.5in|
|PaperA3Rotated|420mm x 297mm|
|PaperA4Rotated|297mm x 210mm|
|PaperA5Rotated|210mm x 148mm|
|PaperJISB4Rotated|B4 (JIS) Rotated 364 x 257 mm|
|PaperJISB5Rotated|B5 (JIS) Rotated 257 x 182 mm|
|PaperJapanesePostcardRotated|Japanese Postcard Rotated 148 x 100 mm|
|PaperJapaneseDoublePostcardRotated|Double Japanese Postcard Rotated 148 x 200 mm|
|PaperA6Rotated|A6 Rotated 148 x 105 mm|
|PaperJapaneseEnvelopeKaku2Rotated|Japanese Envelope Kaku #2 Rotated|
|PaperJapaneseEnvelopeKaku3Rotated|Japanese Envelope Kaku #3 Rotated|
|PaperJapaneseEnvelopeChou3Rotated|Japanese Envelope Chou #3 Rotated|
|PaperJapaneseEnvelopeChou4Rotated|Japanese Envelope Chou #4 Rotated|
|PaperJISB6|B6 (JIS) 128 x 182 mm|
|PaperJISB6Rotated|B6 (JIS) Rotated 182 x 128 mm|
|Paper12x11|12 x 11 in|
|PaperJapaneseEnvelopeYou4|Japanese Envelope You #4|
|PaperJapaneseEnvelopeYou4Rotated|Japanese Envelope You #4 Rotated|
|PaperPRC16K|PRC 16K 146 x 215 mm|
|PaperPRC32K|PRC 32K 97 x 151 mm|
|PaperPRCBig32K|PRC 32K(Big) 97 x 151 mm|
|PaperPRCEnvelope1|PRC Envelope #1 102 x 165 mm|
|PaperPRCEnvelope2|PRC Envelope #2 102 x 176 mm|
|PaperPRCEnvelope3|PRC Envelope #3 125 x 176 mm|
|PaperPRCEnvelope4|PRC Envelope #4 110 x 208 mm|
|PaperPRCEnvelope5|PRC Envelope #5 110 x 220 mm|
|PaperPRCEnvelope6|PRC Envelope #6 120 x 230 mm|
|PaperPRCEnvelope7|PRC Envelope #7 160 x 230 mm|
|PaperPRCEnvelope8|PRC Envelope #8 120 x 309 mm|
|PaperPRCEnvelope9|PRC Envelope #9 229 x 324 mm|
|PaperPRCEnvelope10|PRC Envelope #10 324 x 458 mm|
|PaperPRC16KRotated|PRC 16K Rotated|
|PaperPRC32KRotated|PRC 32K Rotated|
|PaperPRCBig32KRotated|PRC 32K(Big) Rotated|
|PaperPRCEnvelope1Rotated|PRC Envelope #1 Rotated 165 x 102 mm|
|PaperPRCEnvelope2Rotated|PRC Envelope #2 Rotated 176 x 102 mm|
|PaperPRCEnvelope3Rotated|PRC Envelope #3 Rotated 176 x 125 mm|
|PaperPRCEnvelope4Rotated|PRC Envelope #4 Rotated 208 x 110 mm|
|PaperPRCEnvelope5Rotated|PRC Envelope #5 Rotated 220 x 110 mm|
|PaperPRCEnvelope6Rotated|PRC Envelope #6 Rotated 230 x 120 mm|
|PaperPRCEnvelope7Rotated|PRC Envelope #7 Rotated 230 x 160 mm|
|PaperPRCEnvelope8Rotated|PRC Envelope #8 Rotated 309 x 120 mm|
|PaperPRCEnvelope9Rotated|PRC Envelope #9 Rotated 324 x 229 mm|
|PaperPRCEnvelope10Rotated|PRC Envelope #10 Rotated 458 x 324 mm|
|PaperB3|usual B3(13.9 x 19.7 in)|
|PaperBusinessCard|Business Card(90mm x 55 mm)|
|PaperThermal|Thermal(3 x 11 in)|
|Custom|Represents the custom paper size.|
{{< /table >}}

### Print Quality

Set the print quality of the worksheets to be printed with the [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup) class' [PrintQuality](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/printquality) property. The measuring unit for print quality is Dots Per Inches (DPI).

### First Page Number

Start the numbering of worksheet pages using the [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup) class' [FirstPageNumber](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/firstpagenumber) property. The [FirstPageNumber](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/firstpagenumber) property sets the page number of the first worksheet page and the next pages are numbered in ascending order.


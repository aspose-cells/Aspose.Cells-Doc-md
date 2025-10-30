---
title: Expandera text från höger till vänster vid export av Excel fil till HTML
type: docs
weight: 60
url: /sv/python-net/expanding-text-from-right-to-left-while-exporting-excel-file-to/
---

{{% alert color="primary" %}} 

Aspose.Cells för Python via .NET stöder nu utökning av text från höger till vänster vid export av Excel-fil till HTML. Denna funktion har implementerats sedan v8.9.0.0. Om din käll-Excel-fil innehåller text som expanderar från höger till vänster, kommer Aspose.Cells att exportera den korrekt till HTML.

{{% /alert %}} 

## **Expandera text från höger till vänster vid export av Excel-fil till HTML**
Det följande kodexemplet konverterar [provexelfilen](5115502.xlsx) till HTML. Denna skärmbild visar hur provexelfilen ser ut i Microsoft Excel 2013.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

Denna skärmbild visar [utdata-HTML genererad med äldre version](5115509).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

Denna skärmbild visar [utdata-HTML genererad med nyare version](5115508).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

Som du kan se i skärmbilderna, expanderar den nyare versionen den högerjusterade texten till vänster korrekt precis som Microsoft Excel.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExpandTextFromRightToLeft-1.py" >}}
{{< app/cells/assistant language="python-net" >}}

---
title: Lägg till sidfot i flera dokument
type: docs
weight: 80
url: /sv/sharepoint/add-footer-to-multiple-documents/
---

Om du vill lägga till en sidfot i flera Excelfiler ska du välja alternativet ”Lägg till sidfot med Aspose.Cells” i flikfältet.

![todo:image_alt_text](add-footer-to-multiple-documents_1.png)



Hämta alla Excel-filer från datakälla mapp och skapa en filtabell.

Välj filen som behöver få en sidfot, klicka på **Lägg till sidfot**-knappen för att lägga till sidfoten för valda filer. 

![todo:image_alt_text](add-footer-to-multiple-documents_2.png)



Följande alternativ är tillgängliga under konfiguration av sidfoten:

**Sektion**

Lägg till sidfotsposition: Vänster sektion, Mittsektion och Höger sektion.

**Sidfotsskript**

It represents Footer formatting script. Script commands: Command | Description| &P Current page number| &N Page count|&D Current date| &T Current time &A Sheet name &F File name without path &"<FontName>" Font name, for example: &"Arial" &"<FontName>, <FontStyle>" Font name and font style, for example: &"Arial,Bold" &<FontSize> Font size. If this command is followed by a plain number to be printed in the header, it will be separated from the font height with a space character. &G Image script For example: "&Arial,Bold&8Footer Note".

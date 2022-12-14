---
title: Återge Office-tillägg medan du konverterar Excel till PDF
type: docs
weight: 90
url: /sv/java/render-office-add-ins-while-converting-excel-to-pdf/
---
## **Möjliga användningsscenarier**
Tidigare kunde Aspose.Cells inte återge Office-tillägg när Excel-filen sparas i PDF-format. Nu Aspose.Cells gör det bra. Du behöver inte använda någon speciell metod eller egenskap för att rendera Office-tillägg i utdata-PDF. Spara bara din Excel-fil i PDF-format så renderar den Office-tillägg.
## **Återge Office-tillägg medan du konverterar Excel till PDF**
Följande exempelkod sparar[exempel på Excel-fil](60489783.xlsx)som innehåller Office-tilläggen. Vänligen se[output PDF genererad med den tidigare versionen dvs 17.11](60489781.pdf)och den[output PDF genererad med nyare version dvs 17.12 och framåt](60489782.pdf). Den tidigare versionens utdata-PDF är tom men den nyare versionens utdata-PDF visar Office-tillägget.
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-RenderOfficeAdd_InsWhileConvertingExcelToPdf.java" >}}

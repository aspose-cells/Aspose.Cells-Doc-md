---
title: Skapa matrisrapport
type: docs
weight: 10
url: /sv/reportingservices/creating-matrix-report/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services låter dig designa en matris i Microsoft Excel. 

{{% /alert %}} 
### **Mall för matris**
I en Aspose.Cells rapportmall består en matris av hörn, radgrupper, kolumngrupper och dataportioner. En exempelmatris visas nedan.

**En exempelmatris** 

![todo:image_alt_text](creating-matrix-report_1.png)

- **Matrishörn**: som ligger i det övre vänstra hörnet, eller övre högra hörnet för höger-till-vänster (RTL) layouter. Detta område skapas automatiskt när du lägger till både radgrupper och kolumngrupper i en matrisdataposition. I detta område kan du sammanfoga celler i bäddad textruta rapportobjekt.
- **Matrixcolumn grupper area**: som finns i det övre högra hörnet (övre vänstra hörnet för RTL-layout). Detta område skapas automatiskt när du lägger till en kolumngrupp. Cellerna i detta område representerar medlemmar i kolumngrupper, och visar värdena för kolumngruppens instanser. I figuren är cellerna som visar OrderYear en inbäddad kolumngrupp, och cellen som visar OrderQtr är en intilliggande kolumngrupp.
- **Matrixrow grupper area**: som ligger i det nedre vänstra hörnet (nedre högra för RTL-layout). Detta område skapas automatiskt när du lägger till en radgrupp. Cellerna i detta område representerar medlemmar i radgrupper, och visar instansvärden för radgruppen. I figuren är dessa celler inbäddade radgrupper.
- **Matrixdataområde**: som finns i det nedre högra hörnet (nedre vänstra för RTL-layout). Matrisdatan visar detalj- och grupperad data. I detta exempel används endast aggregerad data. Som standard utvärderas cellerna i en grupp rad eller kolumn som innehåller enkla uttryck som inte inkluderar en aggregeringsfunktion till det första värdet i gruppen. I figuren visar cellerna de aggregerade totalerna för radtotaler för alla försäljningsorder.
#### **Skapa en matrismall**
Innan du skapar en matrisrapport, skapa datakällor, dataset och rapportparametrar (valfritt). (Följ anvisningarna i [Datakällor och frågor](/cells/sv/reportingservices/data-sources-and-queries/) om du behöver hjälp.) I exemplet använder vi den medföljande AdventureWorks-provdatabasen som levereras med SQL Server Reporting Services 2008.

För att skapa en ny matris:

1. Öppna Microsoft Excel.
1. Klicka på **Öppna rapport** för att öppna en RDL-rapportfil som innehåller de datakällor, dataset och rapportparametrar som skapats i förväg.
   När filen har öppnats framgångsrikt är all dess information tillgänglig för användning, till exempel listas dess dataset i listan **DataSet**.
1. Öppna ett Microsoft Excel-kalkylblad och välj en datamängd. 

![todo:image_alt_text](creating-matrix-report_2.png)




1. Ange radgrupper och kolumngrupper via **Ange grupp**. 

![todo:image_alt_text](creating-matrix-report_3.png)




1. Sammanfoga celler för att ange matrishörn.

![todo:image_alt_text](creating-matrix-report_4.png)




1. Ange matrishörn genom att infoga en formel. 

![todo:image_alt_text](creating-matrix-report_5.png)




![todo:image_alt_text](creating-matrix-report_6.png)




1. Klicka på **Ange attribut** för att ange matrisattribut. 

![todo:image_alt_text](creating-matrix-report_7.png)



Den består av namn, omfattning, grupp och ordning.

1. Genom att klicka på ändra attribut kontrolleras och ändras alla matrisattribut för aktuell arbetsbok.

![todo:image_alt_text](creating-matrix-report_8.png)




1. Spara, publicera och granska rapporten.

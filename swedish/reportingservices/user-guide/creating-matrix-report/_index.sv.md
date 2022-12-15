---
title: Skapa matrisrapport
type: docs
weight: 10
url: /sv/reportingservices/creating-matrix-report/
---
{{% alert color="primary" %}} 

 Aspose.Cells for Reporting Services låter dig designa en matris i Microsoft Excel.

{{% /alert %}} 
### **Matrix mall**
I en Aspose.Cells rapportmall består en matris av hörn, radgrupper, kolumngrupper och datadelar. En provmatris visas nedan.

**En provmatris** 

![todo:image_alt_text](creating-matrix-report_1.png)

- **Matrix hörn**finns i det övre vänstra hörnet, eller det övre högra hörnet för höger-till-vänster-layouter (RTL). Det här området skapas automatiskt när du lägger till både radgrupper och kolumngrupper till en matrisdataregion. I det här området kan du slå samman inbäddade celler i textrutarapportobjekt.
- **Matris kolumn grupperar område**: finns i det övre högra hörnet (övre vänstra hörnet för RTL-layout). Detta område skapas automatiskt när du lägger till en kolumngrupp. Cellerna i det här området representerar medlemmar i kolumngruppshierarkin och visar kolumngruppens instansvärden. I figuren är cellerna som visar OrderYear en kapslad kolumngrupp, och cellen som visar OrderQtr är en intilliggande kolumngrupp.
- **Matrisradgruppers område**: finns i det nedre vänstra hörnet (nedre höger för RTL-layout). Detta område skapas automatiskt när du lägger till en radgrupp. Cellerna i det här området representerar medlemmar i radgruppshierarkin och visar radgruppsinstansvärden. I figuren är dessa celler kapslade radgrupper.
- **Matrisdataområde**: finns i det nedre högra hörnet (nedre vänster för RTL-layout). Matrisdata visar detaljerade och grupperade data. I det här exemplet används endast aggregerad data. Som standard utvärderas cellerna i en grupprad eller kolumn som innehåller enkla uttryck som inte inkluderar en aggregerad funktion till det första värdet i gruppen. I figuren visar cellerna de sammanlagda summorna för radsummorna för alla försäljningsorder.
#### **Skapa en matrismall**
 Innan du skapar en matrisrapport skapar du datakällorna, datamängderna och rapportparametrarna (valfritt). (Följ instruktionerna i[Datakällor och frågor](/cells/sv/reportingservices/data-sources-and-queries/) om du behöver hjälp.) I exemplet använder vi exempeldatabasen AdventureWorks som levereras med SQL Server Reporting Services 2008.

Så här skapar du en ny matris:

1. Öppna Microsoft Excel.
1.  Klick**Öppna Rapport** för att öppna en RDL-rapportfil som innehåller de datakällor, datamängder och rapportparametrar som skapats i förväg.
När filen väl har öppnats är all information tillgänglig för användning, till exempel listas dess datamängder i**Dataset** lista.
1.  Öppna ett Microsoft Excel-kalkylblad och välj en datamängd.

![todo:image_alt_text](creating-matrix-report_2.png)




1.  Ställ in radgrupper och kolumngrupper**Ställ in grupp**. 

![todo:image_alt_text](creating-matrix-report_3.png)




1. Slå samman celler för att ställa in matrishörn.

![todo:image_alt_text](creating-matrix-report_4.png)




1.  Ställ in matrishörn genom att infoga en formel.

![todo:image_alt_text](creating-matrix-report_5.png)




![todo:image_alt_text](creating-matrix-report_6.png)




1.  Klick**Ställ in attribut** för att ställa in matrisattribut.

![todo:image_alt_text](creating-matrix-report_7.png)



Den består av namn, sortiment, grupp och ordning.

1. Genom att klicka på ändra attribut kontrolleras och ändras alla matrisattribut i det aktuella kalkylbladet.

![todo:image_alt_text](creating-matrix-report_8.png)




1. Spara, publicera och granska rapporten.

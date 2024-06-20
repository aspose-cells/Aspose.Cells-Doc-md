---
title: Aspose.Cells Forms for Sitefinity
type: docs
weight: 10
url: /sv/net/aspose-cells-forms-for-sitefinity/
---

## **Introduktion**

Aspose.Cells Dynamic Forms for Sitefinity Module låter användare generera dynamiska frågeformulär och undersökningar, spara användarinput i Excel-kalkylblad och exportera resultaten till Excel, text, CSV och OpenDocument-kalkylblad med hjälp av Aspose.Cells. Den här modulen visar den kraftfulla kalkylbladsbyggnadsfunktionen som tillhandahålls av Aspose.Cells for .NET.

|<p>![todo:image_alt_text](aspose-cells-forms-for-sitefinity_1)</p><p></p>|
| :- |

### **Modulfunktioner**

Den här inledande versionen av modulen är berikad med följande funktioner för att göra formulärbyggandet och exportprocessen enkel och lätt att använda

- Spara formulärfältinställningar i Excel
- Spara formulärets användarindata i Excel
- Tillåt att lägga till nya och uppdatera befintliga formulärfält
- Tillåt att lägga till TextBox, Multiline TextBox, RadioButtons, CheckBox och DropDownList, DropDownList Items typfält
- Tillåt att lägga till/uppdatera etikett för varje fält
- Tillåt att visa/dölja formulärfält
- Justera automatiskt kolumnerna till innehållslängd och tillämpa rubrikradformatering som Fet text
- Exportera data till Microsoft Excel-dokument (.xls, .xlsx och .xlsb)
- Exportera data till tabbavgränsat textdokument (*.txt)
- Exportera data till CSV (kommaseparerad) (*.csv)
- Exportera data till OpenDocument Spreadsheet (*.ods)
- Alternativ för att välja önskat utdataformat innan exportering.
- Exporterat dokument skickas automatiskt till webbläsaren för nedladdning.

## **Systemkrav och stödda plattformar**

För att konfigurera Aspose.Cells .NET för Sitefinity-tillägg behöver du ha följande krav uppfyllda:

- Sitefinity CMS som körs på ASP.NET 4.0

Tveka inte att kontakta oss om du har några problem med att ställa in detta Sitefinity-tillägg.

Tillägget stöds på alla versioner av

- Sitefinity CMS som körs på ASP.NET 4.0

## **Nerladdning och installation**

### **Nedladdning**

Du kan ladda ner Aspose .NET Content Exporter för Sitefinity-modulen från en av följande platser

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/SiteFinity/Aspose.SiteFinity.FormBuilder.ToExcel)

### **Installation**

När den är nedladdad, följ dessa steg för att installera tillägget i din Sitefinity-webbplats:

**Steg 1: Kopiera filer till din Sitefinity-installation**

Extrahera den nedladdade ZIP-filen. Du kommer att behöva FTP eller direkt åtkomst till Sitefinity-installationsmappen på servern för att utföra följande:

1. Kopiera **Aspose.Cells.dll** & **Aspose.Sitefinity.FormBuilder.dll** till mappen bin inom Sitefinity-installationen.
1. Kopiera mappen **Tillägg** till roten av Sitefinity-installationen där mappen **bin** befinner sig.

**Steg 2: Registrera Aspose Sitefinity Content Export-tillägget i Sitefinity**

1. Log into your Sitefinity CMS with an ‘**Administrator**’ account. The login page can be reached by <http://www.mywebsite.com/sitefinity>
1. Klicka på **Administration** och sedan **Inställningar**.
   Sidans grundinställningar visas.
1. Klicka på länken **Avancerat**.
   Inställningssidan visas.
1. I vänsterfönstret, klicka på **Verktygslådor** följt av **Verktygslådor**, sedan **Sidokontroller**, **Avsnitt** och **Innehållsverktygslådasektion**, sedan **Verktyg**.
1. Klicka på **Skapa ny**.
   Widget-registreringsformuläret visas.
1. Fyll i formulärfälten enligt följande: 
   1. Se till att **Aktiverad** är vald. 
      1. I fältet för **Kontroll CLR-typ eller virtuell sökväg**. 
         1. Lägg till **~/Tillägg/Aspose.SiteFinity.FormBuilder.ToExcel/Edit.ascx**
      1. Lägg till **Namn**, **Titel** och **Beskrivning** enligt följande: 
         1. Aspose  **Sidnamn** (som Edit, View, Export) formulär till SiteFinity-användare
         1. Aspose **Sidnamn** Formulär (som Aspose Redigera formulär , Aspose Visa formulär , Aspose Exportera formulär)
         1. **Sidnamn** Formulär Byggare & Exportör för Sitefinity.
      1. Du kan lämna alla andra fält som de är.
      1. När du är klar, klicka på **Spara ändringar**.
      1. Widgeten är registrerad i verktygslådan och kan användas i Sitefinity. (**Se** **nedan bild**) 

|<p>![todo:image_alt_text](picture1.png)</p><p></p>|
| :- |

## **Användning och videodemonstration**

### **Användning**

När du har installerat och konfigurerat Aspose.Cells Dynamisk Formulärsskapare för Sitefinity-användare är det verkligen enkelt att börja använda det på din webbplats. Följ dessa enkla steg för att komma igång:

1. Se till att du är inloggad på Sitefinity med ett administratörskonto.
1. Navigera till sidan där du vill lägga till pluginen. Se till att sidan är öppen i redigeringsläge.
1. Från menyn **Dra widgetar** till höger, välj Aspose Redigera/Visa/Exportera Formulär och dra den till position. (**Se** **nedan bild**) 

|<p>![todo:image_alt_text](aspose-cells-forms-for-sitefinity_2)</p><p></p>|
| :- |

Du har nu lagt till Aspose.Cells Dynamisk Formulärsskapare för Sitefinity-modulen till din sida.

#### **Hur man tillämpar Aspose License?**

Denna plugin använder en utvärderingsversion av Aspose.Cells. När du är nöjd med din utvärdering kan du köpa en licens på [Aspose Purchase-website](https://purchase.aspose.com/buy).
För att ta bort utvärderingsmeddelandet och begränsningarna för funktioner måste produkten licensieras. Du kommer att få en licensfil efter att du har köpt produkten. Följ stegen nedan för att tillämpa licensen

- Se till att licensfilen är namngiven som **Aspose.Total.lic**
- Placera filen **Aspose.Total.lic** i **App_Data**-mappen på din Sitefinity-webbplats t.ex. "Sitefinity Root-mapp/App_Data/Aspose.Total.lic"

#### **Dynamiska formulärsinställningar**

1. Se till att du är inloggad, klicka på Sidomenyn, klicka på första radens **Visa**-alternativknapp bredvid **Åtgärder-kolumnen.**  
1. Klicka på **Redigera**-knappen som finns bredvid alternativetiketten.
1. Det finns några fördefinierade fält, du kan redigera/dölja genom att helt enkelt klicka på **Redigera** i rutan.
1. Du kan skapa/radera/uppdatera nya fält av vilken typ som helst **(Textruta, FlerradigText, Radioknappar, Kryssrutor, Rullgardinsmeny, Rubrik, Succémeddelande)**

#### **Dynamiskt formulärinskick**

1. Fyll i fälten.
1. Klicka på **Skicka**-knappen för att spara data.
1. Varje klick på **Skicka**-knappen sparar en ny post i Excel.

#### **Exportera sparade data**

1. Se till att du är inloggad, gå till Sidor-meny och klicka på första radens visningsalternativknapp bredvid åtgärdsrutan
1. Hovra över **Exportera ikonen** och klicka på **Exportera** exportera-sidan kommer att öppnas
1. Välj **Exporttyp**
1. Klicka på **Exportera Data**
1. Den exporterade datafilen enligt exporttypen kommer poppa upp för nedladdning/öppning

Du har framgångsrikt lagt till Aspose Sitefinity Export Users to Excel.

### **Video Demonstration**

Var god titta på [videon](https://www.youtube.com/watch?v=La5WMCvafR0) nedan för att se modulen i aktion.

## **Support, Utvidga och Bidra**

### **Support**

Från allra första början av Aspose visste vi att det inte bara skulle räcka med att ge våra kunder bra produkter. Vi behövde också leverera en bra service. Vi är själva utvecklare och förstår hur frustrerande det är när en teknisk fråga eller en egenhet i programvaran hindrar dig från att göra det du behöver göra. Vi är här för att lösa problem, inte skapa dem. 

Detta är anledningen till att vi erbjuder kostnadsfri support. Alla som använder våra produkter, vare sig de har köpt dem eller använder en utvärdering, förtjänar vår fulla uppmärksamhet och respekt.
Du kan logga eventuella problem eller förslag relaterade till Aspose.Cells .NET för Sitefinity-moduler med någon av följande plattformar

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

### **Utvidga och Bidra**

#### **Källkod**

Du kan ladda ner den senaste källkoden på:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET)

#### **Hur man konfigurerar källkoden**

Du måste ha följande installerat för att öppna och utöka källkoden

- Visual Studio 2013 eller högre

Följ dessa enkla steg för att komma igång

1. Ladda ner/Klona källkoden.
1. Öppna Visual Studio 2013 och välj **Arkiv** > **Öppna projekt**
1. Bläddra till den senaste källkoden som du har laddat ner och öppna filen **.sln**.

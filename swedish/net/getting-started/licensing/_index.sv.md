---
title: Licensing
type: docs
weight: 120
url: /sv/net/licensing/
description: Aspose.Cells for .NET tillhandahåller olika planer för köp eller erbjuder en gratis provperiod och en 30-dagars tillfällig licens för utvärdering med Licensing och prenumerationspolicyer i C#.
keywords: C# Apply License from Disk or Stream. C# Set License from Disk or Stream. Apply License in Aspose.Cells for NET.
---
##  **Hur man ansöker om en licens i Aspose.Cells-komponenten**

Licensen är en XML-fil i vanlig text som innehåller detaljer som produktnamn, antal utvecklare den är licensierad till, prenumerationsutgångsdatum och så vidare. Filen är digitalt signerad, så ändra inte filen. Även oavsiktligt tillägg av en extra radbrytning i filen kommer att ogiltigförklara den. Du måste ställa in en licens innan du använder Aspose.Cells om du vill undvika dess utvärderingsbegränsning. Det krävs bara att ställa in en licens en gång per ansökan (eller process). Licensen kan laddas från en fil, stream eller en inbäddad resurs.

Aspose.Cells försöker hitta licensen på följande platser:

- Explicit väg
- Mappen som innehåller Aspose.Cells.dll
- Mappen som innehåller sammansättningen som anropade Aspose.Cells.dll
- Mappen som innehåller postsammansättningen (din .exe)
- En inbäddad resurs i sammansättningen som anropade Aspose.Cells.dll

Det finns två vanliga metoder för att tillämpa en licens, från fil eller stream, eller som en inbäddad resurs.

###  **Hur man ansöker om en licens från disk eller stream**

Det enklaste sättet att ställa in en licens är att lägga licensfilen i samma mapp som den för Aspose.Cells.dll och ange bara filnamnet utan dess sökväg.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

När du anropar SetLicense-metoden bör licensnamnet vara detsamma som för ditt licensfilnamn. Du kan till exempel ändra licensfilens namn till *Aspose.Cells.lic.xml**. Sedan ska du i din kod använda det modifierade licensnamnet (**Aspose.Cells.lic.xml**) för SetLicense-metoden.

{{% /alert %}}

Det är också möjligt att ladda en licens från en stream.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

###  **Hur man ansöker om mätlicens**

Aspose.Cells tillåter utvecklare att använda uppmätt nyckel. Det är en ny licensmekanism. Den nya licensmekanismen kommer att användas tillsammans med den befintliga licensmetoden. De kunder som vill bli fakturerade baserat på användningen av API-funktionerna kan använda den uppmätta licensen. För mer information, se[Mät Licensing FAQ](https://purchase.aspose.com/faqs/licensing/metered)sektion.

En ny klass[Uppmätt](https://reference.aspose.com/cells/net/aspose.cells/metered)har införts för att tillämpa mätt nyckel. Följande är exempelkoden som visar hur man ställer in mätt offentlig och privat nyckel.

{{< highlight "csharp" >}}

 //Set metered public and private keys

Metered metered = new Metered();

//Access the setMeteredKey property and pass public and private keys as parameters

metered.SetMeteredKey("*************", "*************");

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Check if the license is set

Console.WriteLine(workbook.IsLicensed);

//Get the Consumption quantity

decimal amountBefore = Metered.GetConsumptionQuantity();

Console.WriteLine(amountBefore);

Workbook workbook2 = new Workbook("e:\\test2\\Book1.xlsx");

workbook2.Save("e:\\test2\\out1.xlsx");

//Since uploading data is already running on another thread, so you might need to wait for some time (optional)

System.Threading.Thread.Sleep(10000);

//Get the Consumption quantity again which should be greater a bit

decimal amountAfter = Metered.GetConsumptionQuantity();

Console.WriteLine(amountAfter);

{{< /highlight >}}

###  **Hur man använder en inbäddad resurs**

Ett annat snyggt sätt att paketera licensen med din applikation och se till att den inte går förlorad, är att inkludera den som en inbäddad resurs i en av sammansättningarna som anropar Aspose.Cells. För att inkludera licensfilen som en inbäddad resurs, utför följande steg :

1.  I Visual Studio .NET, inkludera licensfilen (.lic) i projektet genom att välja**Lägg till befintligt objekt** från**Fil** meny.
1.  Välj filen i Solution Explorer och ställ in**Bygg Action** till**Inbäddad resurs** i fönstret Egenskaper

För att få åtkomst till licensen som är inbäddad i sammansättningen (som inbäddad resurs) behövs det inte anropas GetExecutingAssembly och GetManifestResourceStream metoder för System.Reflection.Assembly klass Microsoft .NET Framework. Allt du behöver göra är att bara lägga till licensfilen som en inbäddad resurs till ditt projekt och skicka in namnet på licensfilen till SetLicense-metoden. De**Aspose.Cells.License** class hittar automatiskt licensfilen i de inbäddade resurserna. Vänligen granska exemplet nedan för att förstå denna metod för att ställa in licens (inbäddad) i dina applikationer.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

##  **Hur man ställer in licens i Aspose.Cells Grid Controls**

I Aspose.Cells Grid Suite kan licensen laddas från en fil, ström eller en inbäddad resurs. Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb försöker hitta licensen på följande platser:

1. Explicit väg
1. Mappen som innehåller komponentens dll (ingår i Aspose.Cells.GridDesktop eller Aspose.Cells.GridWeb)
1. Mappen som innehåller sammansättningen som anropade komponentens dll (ingår i Aspose.Cells.GridDesktop eller Aspose.Cells.GridWeb)
1. Mappen som innehåller postsammansättningen (din .exe)
1. En inbäddad resurs i sammansättningen som anropade komponentens dll (ingår i Aspose.Cells.GridDesktop eller Aspose.Cells.GridWeb)

{{% alert color="primary" %}}

Om du använder Aspose.Cells.GridDesktop-kontroll kommer licensklassen att användas som Aspose.Cells.GridDesktop.License men om du använder Aspose.Cells.GridWeb-kontroll kommer Aspose.Cells.GridWeb.License-klassen att användas för att ställa in licensen.

{{% /alert %}}

###  **Hur man ansöker om en licens från disk eller stream**

Det enklaste sättet att ställa in en licens är att lägga licensfilen i samma mapp som den för komponentens dll (ingår i Aspose.Cells.GridWeb) och ange bara filnamnet utan dess sökväg.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

När du anropar SetLicense-metoden bör licensnamnet vara detsamma som för ditt licensfilnamn. Du kan till exempel ändra licensfilens namn till "MyLicense.lic.xml". Sedan ska du i din kod använda det modifierade licensnamnet (det vill säga MyLicense.lic.xml) för SetLicense-metoden.

{{% /alert %}}

Det är också möjligt att ladda en licens från en stream.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

###  **Hur man ansöker om en licens som en inbäddad resurs**

Ett annat snyggt sätt att paketera licensen med din applikation och se till att den inte går förlorad, är att inkludera den som en inbäddad resurs i en av assemblyerna som anropar komponentens dll (ingår i Aspose.Cells.GridDesktop). För att inkludera licensfilen som en inbäddad resurs, utför följande steg:

1.  I Visual Studio .NET, inkludera licensfilen (.lic) i projektet med hjälp av**Lägg till befintligt objekt** alternativ på**Fil** meny.
1. Välj filen i Solution Explorer och ställ in Build Action till Embedded Resource i fönstret Egenskaper.
1. För att få åtkomst till licensen som är inbäddad i sammansättningen (som inbäddad resurs) behövs det inte anropas metoderna GetExecutingAssembly och GetManifestResourceStream för klassen System.Reflection.Assembly av Microsoft .NET Framework. Lägg istället till licensfilen som en inbäddad resurs som en inbäddad resurs. projekt och skicka namnet på licensfilen till SetLicense-metoden. Klassen License hittar automatiskt licensfilen i de inbäddade resurserna.

Vänligen granska exemplet nedan för att förstå denna metod för att tillämpa en licens som en inbäddad resurs till dina applikationer.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

##  **Hur man ansöker om en licens i Aspose.Cells.GridDesktop för en WinForm-applikation**

Det rekommenderas att du lägger in din licenskod innan din ansökan startar och att du bara använder den en gång. Till exempel, för ett Windows C#-program, lägg in licenskoden i huvudmetoden.

{{< highlight "csharp" >}}

public class Form1 : System.Windows.Forms.Form

{

private Aspose.Cells.GridDesktop.GridDesktop gridDesktop1;

/// <summary>

/// Required designer variable.

/// </summary>

private System.ComponentModel.Container components = null;

public Form1()

{

//

// Required for Windows Form Designer support

//

InitializeComponent();

//

// TODO: Add any constructor code after InitializeComponent call

//

}

/// The main entry point for the application.

/// </summary>

.

.

.

.

[STAThread]

static void Main()

{

Aspose.Cells.GridDesktop.License lic = new Aspose.Cells.GridDesktop.License();

//Use this line if you are using an explicit path for the license file.

lic.SetLicense(@"C:\MyLicense.lic");

//Or use the line below if you are using the license file as an embedded resource.

//lic.SetLicense("MyLicense.lic");

Application.Run(new Form1());

}

private void Form1_Load(object sender, System.EventArgs e)

{

Aspose.Cells.GridDesktop.Worksheet sheet = this.gridDesktop1.Worksheets.Add("MySheet");

sheet.Cells["A1"].SetCellValue("Hello");

gridDesktop1.ActiveSheetIndex = 1;

}

}

{{< /highlight >}}

##  **Anmärkningar om att tillämpa en licens i Aspose.Cells.GridWeb**

Det rekommenderas att du lägger in licenskoden i Global.asax.cs för din webbapplikation (denna licensfil antas vara placerad på " d:\ "-enheten):

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

Laddar en licens från en ström

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}

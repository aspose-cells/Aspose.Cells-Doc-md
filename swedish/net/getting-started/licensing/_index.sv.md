---
title: Licensiering
type: docs
weight: 120
url: /sv/net/licensing/
description: Aspose.Cells for .NET erbjuder olika planer för köp eller erbjuder en Gratis test och en 30 dagars provlicens för utvärdering med licensiering och prenumerationspolicyer i C#.
keywords: C# Tillämpa licens från disk eller ström. C# Ange licens från disk eller ström. Tillämpa licens i Aspose.Cells for NET.
---

## **Hur man ansöker om en licens i Aspose.Cells-komponenten**

Licensen är en vanlig XML-fil som innehåller detaljer som produktens namn, antal utvecklare som det är licensierat till, prenumerationens utgångsdatum och så vidare. Filen är digitalt signerad, så ändra inte filen. Även oavsiktlig tillägg av en extra radbrytning i filen kommer att ogiltigförklara den. Du behöver ange en licens innan du använder Aspose.Cells om du vill undvika dess utvärderingsbegränsning. Det krävs endast att ange en licens en gång per applikation (eller process). Licensen kan laddas från en fil, ström eller en inbäddad resurs.

Aspose.Cells försöker hitta licensen på följande platser:

- Explicit sökväg
- Mappen som innehåller Aspose.Cells.dll
- Mappen som innehåller sammansättningen som kallade Aspose.Cells.dll
- Mappen som innehåller ingångsammansättningen (din .exe)
- En inbäddad resurs i sammansättningen som kallade Aspose.Cells.dll

Det finns två vanliga metoder för att tillämpa en licens, från en fil eller ström, eller som en inbäddad resurs.

### **Hur man tillämpar en licens från disk eller ström**

Det enklaste sättet att ange en licens är att placera licensfilen i samma mapp som Aspose.Cells.dll och ange bara filnamnet utan dess sökväg.

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

När du anropar SetLicense-metoden bör licensnamnet vara samma som namnet på din licensfil. Till exempel kan du ändra licensfilens namn till **Aspose.Cells.lic.xml**. Sedan i din kod ska du använda det modifierade licensnamnet (**Aspose.Cells.lic.xml**) för SetLicense-metoden.

{{% /alert %}}

Det är också möjligt att ladda en licens från en ström.

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **Hur man ansöker om ett metered licens**

Aspose.Cells tillåter utvecklare att tillämpa meterednyckel. Det är en ny licensieringsmekanism. Den nya licensieringsmekanismen kommer att användas tillsammans med den befintliga licensieringsmetoden. De kunder som vill faktureras utifrån användningen av API-funktionerna kan använda den metered licensieringen. För mer information, vänligen hänvisa till [Metered Licensing FAQ](https://purchase.aspose.com/faqs/licensing/metered) avsnittet.  

En ny klass [Metered](https://reference.aspose.com/cells/net/aspose.cells/metered) har introducerats för att tillämpa en mätad nyckel. Följande är exempelkoden som demonstrerar hur man ställer in en mättad offentlig och privat nyckel.

{{< highlight csharp >}}

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

### **Hur man använder en inbäddad resurs**

Ett annat bra sätt att paketera licensen med din applikation och se till att den inte går förlorad, är att inkludera den som en inbäddad resurs i en av sammansättningarna som kallar Aspose.Cells. För att inkludera licensfilen som en inbäddad resurs, utför följande steg:

1. I Visual Studio .NET, inkludera licensen (.lic) filen i projektet genom att välja **Lägg till befintligt objekt** från **Arkiv**-menyn.
1. Välj filen i Lösningen Utforskaren och ställ in **Byggåtgärd** till **Inbäddad resurs** i Egenskapsfönstret

För att komma åt licensen som är inbäddad i sammansättningen (som inbäddad resurs) behövs det inte att använda System.Reflection.Assembly-klassens GetExecutingAssembly- och GetManifestResourceStream-metoder i Microsoft .NET Framework. Allt som behövs att göra är att helt enkelt lägga till licensfilen som en inbäddad resurs i ditt projekt och skicka namnet på licensfilen till SetLicense-metoden. **Aspose.Cells.License**-klassen hittar automatiskt licensfilen i de inbäddade resurserna. Vänligen granska exemplet nedan för att förstå denna metod för att ställa in licensen (inbäddad) i dina applikationer.

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Hur man ställer in licensen i Aspose.Cells Rutsystem**

I Aspose.Cells Grid Suite kan licensen laddas från en fil, ström eller en inbäddad resurs. Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb försöker hitta licensen på följande platser:

1. Explicit sökväg
1. Mappen som innehåller dll för komponenten (inkluderad i Aspose.Cells.GridDesktop eller Aspose.Cells.GridWeb)
1. Mappen som innehåller sammansättningen som kallade dll för komponenten (inkluderad i Aspose.Cells.GridDesktop eller Aspose.Cells.GridWeb)
1. Mappen som innehåller ingångsammansättningen (din .exe)
1. En inbäddad resurs i sammansättningen som kallade dll för komponenten (inkluderad i Aspose.Cells.GridDesktop eller Aspose.Cells.GridWeb)

{{% alert color="primary" %}}

Om du använder Aspose.Cells.GridDesktop kontrollen kommer licensklassen att användas som Aspose.Cells.GridDesktop.License men om du använder Aspose.Cells.GridWeb kontrollen kommer Aspose.Cells.GridWeb.License klassen att användas för att ställa in licensen.

{{% /alert %}}

### **Hur man tillämpar en licens från disk eller ström**

Det enklaste sättet att ange en licens är att placera licensfilen i samma mapp som dll för komponenten (inkluderad i Aspose.Cells.GridWeb) och ange bara filnamnet utan dess sökväg.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

När du anropar SetLicense-metoden bör licensnamnet vara samma som namnet på din licensfil. Till exempel kan du ändra licensfilens namn till "MyLicense.lic.xml". Sedan i din kod ska du använda det modifierade licensnamnet (det vill säga MyLicense.lic.xml) för SetLicense-metoden.

{{% /alert %}}

Det är också möjligt att ladda en licens från en ström.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **Hur man tillämpar en licens som en inbäddad resurs**

Ett annat bra sätt att paketera licensen med din applikation och se till att den inte försvinner är att inkludera den som en inbäddad resurs i en av de assemblys som anropar dll för komponenten (inkluderad i Aspose.Cells.GridDesktop). För att inkludera licensfilen som en inbäddad resurs, utför följande steg:

1. I Visual Studio .NET, inkludera licensen (.lic) filen i projektet med hjälp av alternativet **Lägg till befintlig post** i menyn **Fil**.
1. Välj filen i Lösning Utforskaren och ställ in Byggåtgärd till Inbäddad Resurs i Egenskapsfönstret.
1. För att komma åt licensen inbäddad i assemblyn (som inbäddad resurs) behöver du inte anropa GetExecutingAssembly och GetManifestResourceStream metoder i Microsoft .NET Framework.System.Reflection.Assembly klass. Lägg istället till licensfilen som en inbäddad resurs i ditt projekt och skicka namnet på licensfilen till SetLicense metoden. Licensklassen hittar automatiskt licensfilen i de inbäddade resurserna.

Vänligen granska exemplet nedan för att förstå denna metod att tillämpa en licens som en inbäddad resurs för dina applikationer.

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

## **Hur man tillämpar en licens i Aspose.Cells.GridDesktop för en WinForm-applikation**

Det rekommenderas att du placerar din licensieringskod innan din applikation startar och tillämpar den endast en gång. Till exempel, för en Windows C#-applikation, placera licensieringskoden i Main-metoden.

{{< highlight csharp >}}

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

## **Noteringar om att tillämpa en licens i Aspose.Cells.GridWeb**

Det rekommenderas att placera licensieringskoden i Global.asax.cs för din webbapplikation (den här licensfilen antas vara placerad på "d:\ " enheten):

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

Ladda en licens från en ström

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}

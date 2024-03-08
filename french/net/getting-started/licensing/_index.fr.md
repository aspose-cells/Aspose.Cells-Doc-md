---
title: Licensing
type: docs
weight: 120
url: /fr/net/licensing/
description: Aspose.Cells for .NET propose différents forfaits à acheter ou propose un essai gratuit et une licence temporaire de 30 jours pour évaluation à l'aide du Licensing et des politiques d'abonnement du C#.
keywords: C# Apply License from Disk or Stream. C# Set License from Disk or Stream. Apply License in Aspose.Cells for NET.
---
##  **Comment appliquer une licence dans le composant Aspose.Cells**

La licence est un fichier XML en texte brut qui contient des détails tels que le nom du produit, le nombre de développeurs auxquels il est concédé sous licence, la date d'expiration de l'abonnement, etc. Le fichier est signé numériquement, ne modifiez donc pas le fichier. Même l'ajout par inadvertance d'un saut de ligne supplémentaire dans le fichier l'invalidera. Vous devez définir une licence avant d'utiliser Aspose.Cells si vous souhaitez éviter sa limitation d'évaluation. Il n'est nécessaire de définir une licence qu'une seule fois par application (ou processus). La licence peut être chargée à partir d'un fichier, d'un flux ou d'une ressource embarquée.

Aspose.Cells essaie de trouver la licence aux emplacements suivants :

- Chemin explicite
- Le dossier qui contient Aspose.Cells.dll
- Le dossier qui contient l'assembly appelé Aspose.Cells.dll
- Le dossier qui contient l'assembly d'entrée (votre .exe)
- Une ressource intégrée dans l'assembly qui a appelé Aspose.Cells.dll

Il existe deux méthodes courantes pour appliquer une licence : à partir d'un fichier ou d'un flux, ou en tant que ressource intégrée.

###  **Comment appliquer une licence à partir d'un disque ou d'un flux**

Le moyen le plus simple de définir une licence consiste à placer le fichier de licence dans le même dossier que celui de Aspose.Cells.dll et à spécifier uniquement le nom du fichier sans son chemin.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

Lorsque vous appelez la méthode SetLicense, le nom de la licence doit être identique à celui de votre fichier de licence. Par exemple, vous pouvez modifier le nom du fichier de licence en *Aspose.Cells.lic.xml**. Ensuite, dans votre code, vous devez utiliser le nom de licence modifié (**Aspose.Cells.lic.xml**) pour la méthode SetLicense.

{{% /alert %}}

Il est également possible de charger une licence depuis un flux.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

###  **Comment demander une licence limitée**

Aspose.Cells permet aux développeurs d’appliquer une clé mesurée. Il s'agit d'un nouveau mécanisme de licence. Le nouveau mécanisme de licence sera utilisé parallèlement à la méthode de licence existante. Les clients qui souhaitent être facturés en fonction de l'utilisation des fonctionnalités API peuvent utiliser la licence limitée. Pour plus de détails, veuillez vous référer à[FAQ Licensing avec compteur](https://purchase.aspose.com/faqs/licensing/metered)section.

Une nouvelle classe[Compteur](https://reference.aspose.com/cells/net/aspose.cells/metered)été introduit pour appliquer une clé mesurée. Voici un exemple de code montrant comment définir une clé publique et privée mesurée.

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

###  **Comment utiliser une ressource intégrée**

Une autre façon intéressante d'emballer la licence avec votre application et de vous assurer qu'elle ne sera pas perdue consiste à l'inclure en tant que ressource intégrée dans l'un des assemblys qui appelle Aspose.Cells. Pour inclure le fichier de licence en tant que ressource intégrée, effectuez les étapes suivantes :

1.  Dans Visual Studio .NET, incluez le fichier de licence (.lic) dans le projet par sélection**Ajouter un article existant** du**Déposer** menu.
1.  Sélectionnez le fichier dans l'Explorateur de solutions et définissez**Créer une action** à**Ressource intégrée** dans la fenêtre Propriétés

Pour accéder à la licence intégrée dans l'assembly (en tant que ressource intégrée), il n'est pas nécessaire d'appeler les méthodes GetExecutingAssembly et GetManifestResourceStream de la classe System.Reflection.Assembly du Framework Microsoft .NET. Tout ce que vous avez à faire est simplement d'ajouter le fichier de licence en tant que ressource intégrée à votre projet et de transmettre le nom du fichier de licence dans la méthode SetLicense. Le**Aspose.Cells.License** la classe trouvera automatiquement le fichier de licence dans les ressources intégrées. Veuillez consulter l'exemple ci-dessous pour comprendre cette méthode de configuration de la licence (intégrée) dans vos applications.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

##  **Comment définir la licence dans les contrôles de grille Aspose.Cells**

Dans Aspose.Cells Grid Suite, la licence peut être chargée à partir d'un fichier, d'un flux ou d'une ressource intégrée. Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb tente de trouver la licence aux emplacements suivants :

1. Chemin explicite
1. Le dossier qui contient la dll du composant (inclus dans Aspose.Cells.GridDesktop ou Aspose.Cells.GridWeb)
1. Le dossier qui contient l'assembly qui a appelé la dll du composant (inclus dans Aspose.Cells.GridDesktop ou Aspose.Cells.GridWeb)
1. Le dossier qui contient l'assembly d'entrée (votre .exe)
1. Une ressource intégrée dans l'assembly qui a appelé la DLL du composant (incluse dans Aspose.Cells.GridDesktop ou Aspose.Cells.GridWeb)

{{% alert color="primary" %}}

Si vous utilisez le contrôle Aspose.Cells.GridDesktop, la classe de licence sera utilisée comme Aspose.Cells.GridDesktop.License, mais si vous utilisez le contrôle Aspose.Cells.GridWeb, la classe Aspose.Cells.GridWeb.License sera utilisée pour définir la licence.

{{% /alert %}}

###  **Comment appliquer une licence à partir d'un disque ou d'un flux**

Le moyen le plus simple de définir une licence est de placer le fichier de licence dans le même dossier que celui de la DLL du composant (inclus dans Aspose.Cells.GridWeb) et de spécifier uniquement le nom du fichier sans son chemin.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

Lorsque vous appelez la méthode SetLicense, le nom de la licence doit être le même que celui de votre fichier de licence. Par exemple, vous pouvez modifier le nom du fichier de licence en « MyLicense.lic.xml ». Ensuite, dans votre code, vous devez utiliser le nom de licence modifié (c'est-à-dire MyLicense.lic.xml) pour la méthode SetLicense.

{{% /alert %}}

Il est également possible de charger une licence depuis un flux.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

###  **Comment appliquer une licence en tant que ressource intégrée**

Une autre façon intéressante d'emballer la licence avec votre application et de vous assurer qu'elle ne sera pas perdue consiste à l'inclure en tant que ressource intégrée dans l'un des assemblys qui appellent la DLL du composant (inclus dans Aspose.Cells.GridDesktop). Pour inclure le fichier de licence en tant que ressource intégrée, effectuez les étapes suivantes :

1.  Dans Visual Studio .NET, incluez le fichier de licence (.lic) dans le projet à l'aide du**Ajouter un article existant** option sur le**Déposer** menu.
1. Sélectionnez le fichier dans l'Explorateur de solutions et définissez l'action de génération sur Ressource intégrée dans la fenêtre Propriétés.
1. Pour accéder à la licence intégrée dans l'assembly (en tant que ressource intégrée), il n'est pas nécessaire d'appeler les méthodes GetExecutingAssembly et GetManifestResourceStream de la classe System.Reflection.Assembly du Framework Microsoft .NET. Au lieu de cela, ajoutez le fichier de licence en tant que ressource intégrée dans votre projet et transmettez le nom du fichier de licence dans la méthode SetLicense. La classe License trouve automatiquement le fichier de licence dans les ressources intégrées.

Veuillez consulter l'exemple ci-dessous pour comprendre cette méthode d'application d'une licence en tant que ressource intégrée à vos applications.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

##  **Comment appliquer une licence dans Aspose.Cells.GridDesktop pour une application WinForm**

Il est recommandé de saisir votre code de licence avant le démarrage de votre application et de l'appliquer une seule fois. Par exemple, pour une application Windows C#, placez le code de licence dans la méthode Main.

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

##  **Notes sur l'application d'une licence dans Aspose.Cells.GridWeb**

Il est recommandé de mettre le code de licence dans le Global.asax.cs de votre application web (ce fichier de licence est supposé être placé sur le lecteur " d:\ ") :

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

Charger une licence à partir d'un flux

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}

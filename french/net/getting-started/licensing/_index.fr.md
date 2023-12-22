---
title: Licensing
type: docs
weight: 120
url: /fr/net/licensing/
description: Aspose.Cells for .NET propose différents forfaits à acheter ou propose un essai gratuit et une licence temporaire de 30 jours pour évaluation à l'aide du Licensing et des politiques d'abonnement du C#.
keywords: Apply License from Disk or Stream. Set License from Disk or Stream. Apply License in Aspose.Cells.
---
{{% alert color="primary" %}}

 Vous pouvez facilement télécharger une version d'évaluation du Aspose.Cells à partir de son[page de téléchargement](https://www.nuget.org/packages/Aspose.Cells) @ NuGet dépôts. La version d'évaluation offre absolument les mêmes fonctionnalités que la version sous licence du composant. De plus, la version d'évaluation devient simplement sous licence lorsque vous achetez une licence et ajoutez quelques lignes de code pour appliquer la licence.

{{% /alert %}}

##  **Limites de la version d'évaluation**

La version d'évaluation du produit Aspose.Cells (sans licence spécifiée) offre toutes les fonctionnalités du produit, mais elle est limitée à l'ouverture de 100 fichiers dans un programme et à une feuille de calcul supplémentaire avec filigrane d'évaluation.

Les limites sont indiquées ci-dessous :

- **Nombre de fichiers ouverts** (Aspose.Cells)
 Lors de l'exécution de votre programme, vous ne pouvez ouvrir que 100 fichiers Excel à l'aide de la bibliothèque Aspose.Cells. Si votre candidature dépasse ce nombre, une exception sera levée.
- **Paramètres du fichier de configuration**(Aspose.Cells.GridWeb)
 Vous ne pouvez pas re-spécifier le chemin du script en ajoutant les lignes de code suivantes dans la section de configuration (par exemple dans le fichier web.config). Le acw_client est un dossier qui contient des fichiers et Aspose.Cells.GridWeb utilise ce dossier pour gérer sa configuration interne, il contient des fichiers de script, des fichiers image et d'autres fichiers pour spécifier le comportement de GridWeb et définir d'autres opérations. Le fichier de configuration est utilisé pour empêcher le contrôle d'utiliser les ressources client intégrées (images, scripts, etc.), ce qui est utile dans certains cas/scénarios. De plus, ces paramètres de configuration dans le fichier web.config ne prendront effet qu'avec la version LICENSED du contrôle.

**XML**

{{< highlight "csharp" >}}

 <appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

Ces paramètres peuvent être obligatoires dans certains cas/scénarios si vous utilisez le contrôle Aspose.Cells.GridWeb dans les sites Web du système de fichiers ou les extensions MS Ajax, etc.

{{% /alert %}}

De plus, une feuille de calcul avec un filigrane d'évaluation s'affichera toujours comme feuille de calcul active dans le fichier Excel généré à l'aide de la bibliothèque Aspose.Cells. Uniquement dans la version sous licence, vous pouvez définir la feuille de calcul active sur d'autres feuilles de calcul. Dans le fichier de sortie PDF ou image par Aspose.Cells, un filigrane d'évaluation sera collé en haut du document/image. Vous ne pouvez pas non plus masquer l'avertissement de copyright d'évaluation (la feuille de calcul supplémentaire) dans le contrôle GridWeb, il sera toujours ajouté. (à la fin dans les onglets de la feuille de calcul) dans le champ.

{{% alert color="primary" %}}

 Si vous souhaitez tester le Aspose.Cells sans limitations de la version d'évaluation, vous pouvez également demander un[Permis temporaire de 30 jours](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

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

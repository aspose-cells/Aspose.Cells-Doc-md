---
title: Utilisation de Aspose.Cells.GridDesktop dans l'application WPF
type: docs
weight: 50
url: /fr/net/using-aspose-cells-griddesktop-in-wpf-application/
---
{{% alert color="primary" %}} 

 Cet article montre comment utiliser le concepteur Windows Presentation Foundation (WPF) pour Visual Studio pour héberger un contrôle Forms Windows tel que Aspose.Cells.GridDesktop dans une application WPF.
Nous utiliserons Visual Studio 2015 pour démontrer le processus, cependant, vous pouvez utiliser n'importe quelle version, y compris Visual Studio 2008 ou une version ultérieure.

{{% /alert %}} 

Ce didacticiel vous guidera tout au long du processus d'ajout du contrôle Aspose.Cells.GridDesktop à une application WPF. Vous avez besoin de n'importe quelle version de l'IDE de Visual Studio qui prend en charge le développement WPF afin d'essayer cela de votre côté.
## **Créer une application WPF à l'aide de Visual Studio**
 Créez d'abord une application WPF à l'aide de Visual Studio IDE. Cliquer sur**Dossier** >> **Nouveau** >> **Projet** menu et sélectionnez**Application WPF** dans Modèles, nommez le projet et cliquez sur**D'ACCORD**. Vous pouvez cibler votre projet sur n'importe quel framework .NET supérieur à 2.0, cependant, vous ne pouvez pas utiliser le profil client .NET Frameworks.
## **Ajouter des références aux espaces de noms requis**
Ajoutez les références aux assemblys suivants en cliquant avec le bouton droit sur la fenêtre Références de l'Explorateur de solutions et sélectionnez le menu Ajouter une référence.

- Assembly WindowsFormsIntegration (WindowsFormsIntegration.dll).
- Windows Assemblage de formulaires (System.Windows.Forms.dll).
- Aspose.Cells.Assemblage GridDesktop (Aspose.Cells.GridDesktop.dll).

Cette action ajoute les assemblys requis à l'application, c'est-à-dire ; copie les assemblys dans le dossier Bin de l'application.
## **Ajouter des références à XAML**
Ensuite, accédez au fichier XAML et ajoutez les espaces de noms et références d'assembly suivants dans la balise Windows.

{{< highlight "java" >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**La balise finale Windows ressemblera à celle illustrée ci-dessous.**

![tâche : image_autre_texte](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **Ajouter le contrôle Aspose.Cells.GridDesktop à XAML**
 Ajoutez simplement le code ci-dessous dans la balise Grid en XAML. Le**WindowsFormsHostWindowsFormsHost** la balise est utilisée pour héberger le contrôle des formulaires Windows et**gridDesktop:GridDesktop** La balise représente le contrôle Aspose.Cells.GridDesktop. Vous pouvez également nommer le contrôle afin qu'il puisse être facilement référencé dans le code.

{{< highlight "java" >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**Le XAML final se présentera comme suit.** 

![tâche : image_autre_texte](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **Utilisez Aspose.Cells.GridDesktop**
Nous pouvons désormais accéder et utiliser le contrôle Aspose.Cells.GridDesktop dans le fichier .cs comme toute autre application Windows Forms. Afin de simplifier la démonstration, nous chargeons simplement un exemple de feuille de calcul dans le contrôle Aspose.Cells.GridDesktop et l'enregistrons à nouveau. De plus, nous avons utilisé l'événement FrameworkElement_OnLoaded pour déclencher les instructions suivantes.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **Construire et exécuter**
 Maintenant, construisez et exécutez l'application en utilisant**F5** ou alors**Démarrer** bouton sur l'interface utilisateur de Visual Studio.

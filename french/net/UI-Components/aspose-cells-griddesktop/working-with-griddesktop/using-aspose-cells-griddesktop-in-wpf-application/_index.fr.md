---
title: Utilisation de Aspose.Cells.GridDesktop dans une application WPF
type: docs
weight: 50
url: /fr/net/aspose-cells-griddesktop/use-aspose-cells-griddesktop-in-wpf-application/
keywords: GridDesktop,wpf
description: Cet article présente comment utiliser GridDesktop dans une application WPF.
---

{{% alert color="primary" %}} 

Cet article montre comment utiliser le concepteur de Windows Presentation Foundation (WPF) pour Visual Studio afin d'héberger un contrôle Windows Forms tel que Aspose.Cells.GridDesktop dans une application WPF. 
Nous utiliserons Visual Studio 2015 pour illustrer le processus, cependant, vous pouvez utiliser n'importe quelle version, y compris Visual Studio 2008 ou ultérieure.

{{% /alert %}} 

Ce tutoriel vous guidera à travers le processus d'ajout du contrôle Aspose.Cells.GridDesktop à une application WPF. Vous avez besoin de n'importe quelle version de l'IDE Visual Studio prenant en charge le développement WPF pour essayer cela de votre côté.
## **Créez une application WPF en utilisant Visual Studio**
Commencez par créer une application WPF en utilisant l'IDE Visual Studio. Cliquez sur **Fichier** >> **Nouveau** >> **Projet** et sélectionnez **Application WPF** dans les modèles, nommez le projet et cliquez sur **OK**. Vous pouvez cibler votre projet vers n'importe quelle version du framework .NET supérieure à 2.0, cependant, vous ne pouvez pas utiliser les profils client des frameworks .NET.
## **Ajoutez des références aux espaces de noms requis**
Ajoutez les références aux assemblies suivants en cliquant avec le bouton droit sur les Références depuis la fenêtre de l'Explorateur de solutions et en sélectionnant le menu Ajouter une référence.

- Assembly WindowsFormsIntegration (WindowsFormsIntegration.dll).
- Assembly Windows Forms (System.Windows.Forms.dll).
- Assembly Aspose.Cells.GridDesktop (Aspose.Cells.GridDesktop.dll).

Cette action ajoute les assemblies requis à l'application, c'est-à-dire copie les assemblies dans le dossier Bin de l'application.
## **Ajoutez des références à XAML**
Ensuite, accédez au fichier XAML et ajoutez les espaces de noms et les références d'assembly suivants dans la balise Windows.

{{< highlight java >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**La balise Windows finale ressemblera à ce qui suit.**

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **Ajoutez le contrôle Aspose.Cells.GridDesktop au XAML**
Ajoutez simplement le code ci-dessous à l'intérieur de la balise Grid dans le XAML. La balise **WindowsFormsHost** est utilisée pour héberger le contrôle Windows Forms et la balise **gridDesktop:GridDesktop** représente le contrôle Aspose.Cells.GridDesktop. Vous pouvez également nommer le contrôle de manière à ce qu'il puisse être facilement référencé dans le code.

{{< highlight java >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**Le XAML final ressemblera comme suit.** 

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **Utilisez Aspose.Cells.GridDesktop**
Nous pouvons maintenant accéder et utiliser le contrôle Aspose.Cells.GridDesktop dans le fichier .cs comme n'importe quelle autre application Windows Forms. Afin de maintenir la démonstration simple, nous chargeons simplement une feuille de calcul d'exemple dans le contrôle Aspose.Cells.GridDesktop et la sauvegardons. De plus, nous avons utilisé l'événement FrameworkElement_OnLoaded pour déclencher les déclarations suivantes.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **Construire et exécuter**
Maintenant, construisez et exécutez l'application en utilisant le bouton **F5** ou **Démarrer** sur l'interface utilisateur de Visual Studio.

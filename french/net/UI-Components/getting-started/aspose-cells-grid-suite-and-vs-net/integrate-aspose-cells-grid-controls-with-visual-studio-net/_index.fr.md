---
title: Intégrez les contrôles de grille Aspose.Cells avec Visual Studio.NET
type: docs
weight: 10
url: /fr/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/
description: Cet article décrit comment utiliser les contrôles GridWeb et GridDesktop dans vissual studio .NET.
keywords:  GridWeb,GridDesktop,visual studio,control,integrate
---

{{% alert color="primary" %}} 

Les développeurs de Visual Studio.NET peuvent facilement faire glisser des contrôles depuis la **Boîte à outils** sur un formulaire Windows ou Web. Aspose.Cells Grid suite peut être téléchargé avec un installateur MSI ou en tant que package de DLLs. Cet article explique quoi faire pour s'assurer que les contrôles Aspose.Cells.Grid peuvent être utilisés dans Visual Studio.NET lorsqu'ils sont installés en utilisant les DLLs au lieu de l'installateur.

{{% /alert %}} 
## **Intégrer les contrôles Aspose.Cells Grid avec Visual Studio.NET**
Pour intégrer les contrôles Aspose.Cells Grid avec Visual Studio.NET :

1. Ouvrez la Boîte à outils.
1. Sélectionnez l'onglet Général (ou tout autre onglet où vous voulez ajouter des contrôles).
1. Cliquez avec le bouton droit sur l'onglet Général.
1. Sur Visual Studio.NET, sélectionnez **Choose Items** dans le menu. La boîte de dialogue Personnaliser la boîte à outils apparaîtra (ce processus est plus ou moins le même pour les nouveaux IDE VS.NET (par exemple VS.NET 2013/2015 ou ultérieur)).
1. Cliquez sur **Parcourir** et localisez les fichiers Aspose.Cells.GridDesktop.dll et Aspose.Cells.GridWeb.dll.
1. Sélectionnez les DLLs, puis cliquez sur **Ouvrir**. La boîte de dialogue Personnaliser la boîte à outils contiendra maintenant des contrôles de Aspose.Cells Grid Suite. Les nouveaux contrôles ajoutés seront mis en surbrillance par la boîte de dialogue.
1. Cliquez sur **OK** pour ajouter les contrôles à votre Boîte à outils Visual Studio.NET.

Les contrôles Aspose.Cells Grid seront ajoutés à l'onglet **Général** de la Boîte à outils. Seul le contrôle GridWeb n'est pas actif. Cela est dû au fait que nous travaillons sur une application Windows Forms. GridWeb n'est disponible que lorsque vous travaillez sur des formulaires Web, tandis que GridDesktop peut être utilisé uniquement avec des formulaires Windows.

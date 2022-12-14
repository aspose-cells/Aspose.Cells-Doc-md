---
title: Intégrer les contrôles de grille Aspose.Cells à Visual Studio.NET
type: docs
weight: 10
url: /fr/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/
---
{{% alert color="primary" %}} 

 Les développeurs Visual Studio.NET peuvent facilement faire glisser des contrôles depuis le**Boîte à outils** sur un formulaire Windows ou Web. Aspose.Cells La suite Grid peut être téléchargée avec un programme d'installation MSI ou sous la forme d'un ensemble de packages DLL. Cet article explique ce qu'il faut faire pour s'assurer que les contrôles Aspose.Cells.Grid peuvent être utilisés dans Visual Studio.NET lorsqu'il est installé à l'aide des DLL au lieu du programme d'installation.

{{% /alert %}} 
## **Intégrer les contrôles de grille Aspose.Cells à Visual Studio.NET**
Pour intégrer les contrôles Grid Aspose.Cells à Visual Studio.NET :

1. Ouvrez la boîte à outils.
1. Sélectionnez l'onglet Général (ou tout autre onglet auquel vous souhaitez ajouter des contrôles).
1. Cliquez avec le bouton droit sur l'onglet Général.
1.  Sur Visual Studio.NET 2003 : sélectionnez**Ajouter/supprimer des éléments** du menu.
1. Sur Visual Studio.NET 2005, sélectionnez**Choisissez des articles** du menu. La boîte de dialogue Personnaliser la boîte à outils apparaîtra (ce processus est plus ou moins le même pour les nouveaux IDE VS.NET (par exemple VS.NET 2013/2015 ou version ultérieure)).
1.  Cliquez sur**Parcourir** et localisez les fichiers Aspose.Cells.GridDesktop.dll et Aspose.Cells.GridWeb.dll.
1.  Sélectionnez les DLL, puis cliquez sur**Ouvert**. La boîte de dialogue Personnaliser la boîte à outils contiendra désormais les commandes de Aspose.Cells Grid Suite. Les contrôles nouvellement ajoutés seront mis en évidence par la boîte de dialogue.
1.  Cliquez sur**D'ACCORD** pour ajouter les contrôles à votre boîte à outils Visual Studio.NET.

 les contrôles de grille Aspose.Cells auront été ajoutés à la boîte à outils**Général** languette. Seul le champ GridWeb n'est pas actif. C'est parce que nous travaillons sur une application Windows Forms. GridWeb n'est disponible que lorsque vous travaillez sur des formulaires Web, tandis que GridDesktop ne peut être utilisé qu'avec les formulaires Windows.

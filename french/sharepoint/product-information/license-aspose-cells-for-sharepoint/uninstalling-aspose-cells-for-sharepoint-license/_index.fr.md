---
title: Désinstallation de la Licence Aspose.Cells for SharePoint
type: docs
weight: 30
url: /fr/sharepoint/uninstalling-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}} 

Pour désinstaller la licence Aspose.Cells for SharePoint, veuillez suivre les étapes ci-dessous à partir de la console du serveur. 

{{% /alert %}} 

1. Retirez la solution de licence de la ferme :
   stsadm.exe -o retractsolution -name Aspose.Cells.SharePoint.License.wsp -immediate
1. Exécutez les travaux d'administration pour terminer immédiatement la rétraction :
   stsadm.exe -o execadmsvcjobs
1. Attendre la rétractation pour se terminer.
   Vous pouvez utiliser l'Administration centrale pour vérifier si la rétractation est terminée en allant à **l'Administration centrale**, puis **Opérations** et **Gestion de solutions**.
1. Retirer la solution de la bibliothèque de solutions SharePoint :
   stsadm.exe -o deletesolution -name Aspose.Cells.SharePoint.License.wsp

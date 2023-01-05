---
title: Désinstallation de la licence Aspose.Cells for SharePoint
type: docs
weight: 30
url: /fr/sharepoint/uninstalling-aspose-cells-for-sharepoint-license/
---
{{% alert color="primary" %}} 

 Pour désinstaller la licence Aspose.Cells for SharePoint, veuillez suivre les étapes ci-dessous à partir de la console du serveur.

{{% /alert %}} 

1. Retirez la solution de licence de la batterie :
 stsadm.exe -o retractsolution -name Aspose.Cells.SharePoint.License.wsp -immediate
1. Exécutez les travaux du minuteur d'administration pour terminer la rétractation immédiatement :
 stsadm.exe -o execadmsvcjobs
1. Attendez que la rétraction soit terminée.
 Vous pouvez utiliser l'Administration centrale pour vérifier si la rétractation est terminée en accédant à**Administration centrale** , ensuite**Opérations** et**Gestion des solutions**.
1. Supprimez la solution du magasin de solutions SharePoint :
 stsadm.exe -o deletesolution -name Aspose.Cells.SharePoint.License.wsp

---
title: Sous rapport
type: docs
weight: 90
url: /fr/reportingservices/sub-report/
---

{{% alert color="primary" %}} 

Un sous-rapport peut être intégré dans un élément de tableau. Le format est: &=subreport{ReportName=nom de votre rapport; nom du paramètre 1 = valeur du paramètre 1; nom du paramètre 2 = valeur du paramètre 2; ...}

**Un sous-rapport dans une définition de rapport** 

![todo:image_alt_text](sub-report_1.png)

Dans l'exemple, le nom du sous-rapport est "Détail de la commande de vente". Il possède un paramètre, SalesOrderNumber. La valeur du paramètre est EmpSalesDetail.SalesOrderNumber.
### **Restrictions sur les sous-rapports**
1. Le sous-rapport doit être conçu avec Aspose.Cells.ReportingServices Designer.
1. Le sous-rapport ne peut être intégré que dans la ligne du groupe de table, et la ligne de groupe ne peut contenir aucun élément excepté le sous-rapport. Il n'est pas autorisé d'intégrer un sous-rapport dans les lignes de détail ou les lignes de pied de table.
1. Actuellement, l'imbrication de plus d'un niveau n'est pas prise en charge. Le sous-rapport ne peut pas contenir de rapport intégré.

{{% /alert %}} 
###### **Cette section comprend les sujets suivants :** 
- [Création de l'élément de tableau](/cells/fr/reportingservices/creating-table-item/)
- [Ajouter un élément de sous-rapport](/cells/fr/reportingservices/add-sub-report-item/)

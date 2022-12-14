---
title: Sous-rapport
type: docs
weight: 90
url: /fr/reportingservices/sub-report/
---
{{% alert color="primary" %}} 

Un sous-rapport peut être intégré dans un élément de tableau. Le format est : &=subreport{ReportName=votre nom de rapport ; nom du paramètre1 = valeur du paramètre1 ; nom du paramètre2 = valeur du paramètre2 ; ...}

**Un sous-rapport dans une définition de rapport** 

![tâche : image_autre_texte](sub-report_1.png)

Dans l'exemple, le nom du sous-rapport est "Sales Order Detail". Il a un paramètre, SalesOrderNumber. La valeur du paramètre est EmpSalesDetail.SalesOrderNumber.
### **Restrictions sur les sous-rapports**
1. Le sous-rapport doit être conçu avec Aspose.Cells.ReportingServices Designer.
1. Le sous-rapport ne peut être intégré que dans la ligne du groupe de tableaux et la ligne du groupe ne peut contenir aucun élément à l'exception du sous-rapport. L'intégration d'un sous-rapport dans les lignes de détail du tableau ou les lignes de pied de page n'est pas autorisée.
1. Actuellement, l'imbrication de plusieurs niveaux n'est pas prise en charge. Le sous-rapport ne peut pas contenir de rapport intégré.

{{% /alert %}} 
###### **Cette section comprend les rubriques suivantes :**
- [Création d'un élément de table](/cells/fr/reportingservices/creating-table-item/)
- [Ajouter un élément de sous-rapport](/cells/fr/reportingservices/add-sub-report-item/)

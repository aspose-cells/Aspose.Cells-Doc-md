---
title: Remplissage d un fichier .jasper avec prise en charge de graphique modifiable
type: docs
weight: 10
url: /fr/jasperreports/filling-a-jasper-file-with-editable-chart-support/
---

{{% alert color="primary" %}} 

Aspose.Cells for JasperReports nécessite qu'un fichier .jasper soit rempli par un .jrprint ou un objet JasperPrint avant qu'il puisse être exporté vers un fichier XLS. Aucune modification n'est nécessaire pour le fichier .jrxml. La procédure de remplissage stocke les représentations internes des graphiques dans l'objet JasperPrint qui est ensuite utilisé pour générer des graphiques modifiables. 

{{% /alert %}} 

Veuillez lire la documentation de JasperReports pour une description détaillée de comment remplir un rapport.

Voici un exemple :

**Java**

{{< highlight csharp >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}

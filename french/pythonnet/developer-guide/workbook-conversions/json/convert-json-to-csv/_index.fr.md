---
title: Convertir JSON en CSV
type: docs
weight: 210
url: /fr/python-net/convert-json-to-csv/
description: Apprenez comment convertir un fichier JSON en fichier CSV avec l API Aspose.Cells pour Python via .NET.
keywords: Python Convertir json en csv, Conversion de fichier json en csv avec Python via NET, Exporter json en csv, Convertir un fichier json en csv
---

## **Convertir JSON en CSV**

Aspose.Cells pour Python via .NET prend en charge la conversion de JSON simple ainsi que de JSON imbriqué en CSV. Pour cela, l'API fournit les classes [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) et [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility). La classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) fournit les options pour la mise en page JSON comme [**ignore_array_title**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/ignore_array_title/) (ignore le titre si le tableau est une propriété d'un objet) ou [**array_as_table**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/array_as_table/) (traite le tableau comme un tableau). La classe [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) traite le JSON en utilisant les options de mise en page définies avec la classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions).

Le code d'exemple suivant démontre l'utilisation des classes [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) et [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) pour charger le [fichier JSON source](104398869.json) et générer le [fichier CSV en sortie](104398870.csv).

### **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.py" >}}

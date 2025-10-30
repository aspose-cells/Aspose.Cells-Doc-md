---
title: Wie man Series mit Python.NET unsichtbar macht
linktitle: Wie man Serien unsichtbar macht
type: docs
weight: 74
url: /de/python-net/how-to-set-series-invisible/
description: Erfahren Sie, wie Sie Diagrammserien in Excel mit Aspose.Cells für Python via .NET Schritt für Schritt ausblenden können.
keywords: Python Excel Diagramm, Serie ausblenden, `is_filtered` Eigenschaft, Aspose.Cells Python
---

## **Wie man Serien in Excel-Diagrammen unsichtbar macht**

In einem Excel-Diagramm können Sie mit der rechten Maustaste auf das Diagramm klicken, "Daten auswählen" auswählen und im Pop-up-Fenster festlegen, ob eine Serie sichtbar sein soll, indem Sie sie aktivieren oder deaktivieren.
Sie können die folgende [Musterdaten-Datei](SeriesFiltered.xlsx) herunterladen und in Excel wie in der Abbildung gezeigt verwenden, um diese Funktion zu erreichen. Als nächstes zeigen wir Ihnen, wie Sie dies mit der Aspose.Cells für Python via .NET-Bibliothek realisieren.

![todo:image_alt_text](series-invisible.png)

## **Wie man Serien mit Aspose.Cells unsichtbar macht**

Verwenden Sie den folgenden Code, um Serien mit Aspose.Cells für Python via .NET unsichtbar zu machen:

```python
import os
from aspose.cells import Workbook

current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Load sample workbook
workbook = Workbook(os.path.join(data_dir, "SeriesFiltered.xlsx"))

# Access charts from first worksheet
charts = workbook.worksheets[0].charts
chart = charts.get("Chart 1")

# Get series collections
n_series_filtered = chart.filtered_n_series
n_series = chart.n_series

# Filter series by marking them as filtered
n_series[1].is_filtered = True
n_series[0].is_filtered = True

# Save modified workbook
workbook.save(os.path.join(data_dir, "output.xlsx"))
```

Sie können die folgende [Inputdatei](SeriesFiltered.xlsx) und [Ausgabedatei](output.xlsx) erhalten.

Wie im unteren Bild gezeigt, sind die ersten beiden Serien, die ursprünglich sichtbar waren, im Ausgabedokument unsichtbar geworden.
![todo:image_alt_text](output.png)
{{< app/cells/assistant language="python-net" >}}

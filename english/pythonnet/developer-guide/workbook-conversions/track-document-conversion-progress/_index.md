---
title: Track Document Conversion Progress with Python via .NET
linktitle: Track Document Conversion Progress
type: docs
weight: 970
url: /python-net/track-document-conversion-progress/
description: Learn how to monitor Excel file conversion progress using Aspose.Cells for Python via .NET API with page saving callbacks.
---

## **Possible Usage Scenarios**

Sometimes converting large Excel files can take some time. During this time, you might want to show the document conversion progress instead of just a loading screen to enhance the usability of your application. Aspose.Cells supports tracking document conversion process by providing the [**IPageSavingCallback**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/ipagesavingcallback) abstract base class. The [**IPageSavingCallback**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/ipagesavingcallback) class provides [**page_start_saving**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/ipagesavingcallback/page_start_saving/) and [**page_end_saving**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/ipagesavingcallback/page_end_saving/) methods that you can implement in your custom class. You may also control which pages are rendered as demonstrated in the *TestPageSavingCallback* custom class.

## **Track Document Conversion Progress**

The following code sample loads the [source Excel file](94896151.xlsx) and prints its conversion progress in the console by using the *TestPageSavingCallback* custom class that implements the [**IPageSavingCallback**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/ipagesavingcallback) abstract base class.

## **Sample Code**

```python
import os
from aspose.cells import Workbook, PdfSaveOptions
from aspose.cells.rendering import IPageSavingCallback

class TestPageSavingCallback(IPageSavingCallback):
    def page_saving(self, args):
        pass

# Source directory
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "source")
# Output directory
output_dir = os.path.join(current_dir, "output")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

workbook = Workbook(os.path.join(source_dir, "PagesBook1.xlsx"))
pdf_save_options = PdfSaveOptions()
pdf_save_options.page_saving_callback = TestPageSavingCallback()

workbook.save(os.path.join(output_dir, "DocumentConversionProgress.pdf"), pdf_save_options)
```

```python
from aspose.cells import IPageSavingCallback, PageStartSavingArgs, PageEndSavingArgs

class TestPageSavingCallback(IPageSavingCallback):
    def page_start_saving(self, args: PageStartSavingArgs):
        print(f"Start saving page index {args.page_index} of pages {args.page_count}")
        
        # Don't output pages before page index 2
        if args.page_index < 2:
            args.is_to_output = False
    
    def page_end_saving(self, args: PageEndSavingArgs):
        print(f"End saving page index {args.page_index} of pages {args.page_count}")
        
        # Don't output pages after page index 8
        if args.page_index >= 8:
            args.has_more_pages = False
```

## **Console Output**

{{< highlight plaintext >}}
Start saving page index 0 of pages 11
End saving page index 0 of pages 11
Start saving page index 1 of pages 11
End saving page index 1 of pages 11
Start saving page index 2 of pages 11
End saving page index 2 of pages 11
Start saving page index 3 of pages 11
End saving page index 3 of pages 11
Start saving page index 4 of pages 11
End saving page index 4 of pages 11
Start saving page index 5 of pages 11
End saving page index 5 of pages 11
Start saving page index 6 of pages 11
End saving page index 6 of pages 11
Start saving page index 7 of pages 11
End saving page index 7 of pages 11
Start saving page index 8 of pages 11
End saving page index 8 of pages 11
{{< /highlight >}}
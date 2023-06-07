---
title: Headings And Body Theme Font
type: docs
weight: 120
url: /net/headings-and-body-Theme-font/
---

{{% alert color="primary" %}}

The default font will automatically change when the regoin setting is changed. 

If the default font is changed, the row height and column width is also changed, and it may even mess up the page layout.

What caused the default font to change?

If Excel theme font is set, Excel will automatically switch between different fonts based on the current language environment.


{{% /alert %}}

## **Headings And Body Theme Font In Excel**

In Excel, select Home tab, click on the font dropdown box ,you will see "Theme Fonts" with two theme fonts : Calibri Light (Headings) and Calibri (Body) on the top with English region setting.

**![Theme Fonts](Theme-Fonts.png)**

If Theme Font is selected, the file will display file displays different in different regions .
If you do not want to automitally change font in different regions, don't select The two Theme Fonts .


## **Changing Headings And Body Font Programally**
With Aspose.Cells for .Net , we can check whether the default font is theme font or set theme font with  [**Font.SchemeType**](https://reference.aspose.com/cells/net/aspose.cells/font/schemetype/) property.

The following sample code shows how to manipulate theme font.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Headings-and-body-font.cs" >}}


## **Dynamically Gets Local Theme Font Programally**
Sometimes, our servers and users' machines are not in the same region. How can we obtain the same font that users want for file processing?

We have to set the system regional settings before loading the file with [**LoadOptions.Region**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/region/) property

The following sample code shows how to get local theme font.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Local-Theme-Font.cs" >}}
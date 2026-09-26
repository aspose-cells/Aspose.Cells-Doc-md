---
title: Calculate Page Setup Scaling Factor with Golang via C++
linktitle: Calculate Page Setup Scaling Factor
type: docs
weight: 300
url: /go-cpp/calculate-page-setup-scaling-factor/
description: This article provides sample code explaining how to use the Go API or library to calculate Page Setup scaling factor using Fit to n page(s) wide by m tall option of Excel worksheet programmatically.
keywords: Fit to n page wide by m tall excel c++, calculate page setup scaling factor c++
---

{{% alert color="primary" %}}

When you set Page Setup Scaling using **Fit to n page(s) wide by m tall** option, Microsoft Excel calculates the Page Setup Scaling Factor. You can calculate the same value using [**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/go-cpp/sheetrender/getpagescale/) property. This property returns a double value which can be converted to a percentage value. For example, if it returns 0.5, then it means that the scaling factor is 50%.

{{% /alert %}}

The following sample code illustrates how to calculate page setup scaling factor using [**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/go-cpp/sheetrender/getpagescale/) property.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculatePageSetupScalingFactor.go" >}}
{{< app/cells/assistant language="go" >}}

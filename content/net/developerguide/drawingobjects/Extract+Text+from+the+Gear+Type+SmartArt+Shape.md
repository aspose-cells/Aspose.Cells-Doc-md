+++
title = "Extract Text from the Gear Type SmartArt Shape" 
description = "" 
weight = 12285 
+++

Aspose.Cells for .NET : Extract Text from the Gear Type SmartArt Shape  

# Aspose.Cells for .NET : Extract Text from the Gear Type SmartArt Shape


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#ExtractTextfromtheGearTypeSmartArtShape-PossibleUsageScenarios)
*   2 [Extract Text from the Gear Type SmartArt Shape](#ExtractTextfromtheGearTypeSmartArtShape-ExtractTextfromtheGearTypeSmartArtShape)
*   3 [Sample Code](#ExtractTextfromtheGearTypeSmartArtShape-SampleCode)
*   4 [Console Output](#ExtractTextfromtheGearTypeSmartArtShape-ConsoleOutput)
{{< /panel >}}
 

## Possible Usage Scenarios

Aspose.Cells can extract text from the `Gear Type Smart Art Shape`. In order to do so, you should first convert `Smart Art Shape` to `Group Shape` using the [Shape.GetResultOfSmartArt()](https://apireference.aspose.com/net/cells/aspose.cells.drawing/shape/methods/getresultofsmartart) method. Then you should get the array of all the `Individual Shapes` forming the Group Shape using the [GroupShape.GetGroupedShapes()](https://apireference.aspose.com/net/cells/aspose.cells.drawing/groupshape/methods/getgroupedshapes) method. Finally, you can iterate all of the Individual Shapes one by one in a loop and extract their text using the [Shape.Text](https://apireference.aspose.com/net/cells/aspose.cells.drawing/shape/properties/text) property.

## Extract Text from the Gear Type SmartArt Shape

The following sample code loads the [sample Excel file](https://docs2.aspose.com/cells/net/attachments/66948394/67338483.xlsx) that contains `Gear Type Smart Art Shape`. It then extracts the text from its individual shapes as discussed above. Please see the console output of the code given below for a reference.

## Sample Code

## Console Output

{{< code lang="cs" >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /code >}}

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sampleExtractTextFromGearTypeSmartArtShape.xlsx](https://docs2.aspose.com/cells/net/attachments/66948394/67338483.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  


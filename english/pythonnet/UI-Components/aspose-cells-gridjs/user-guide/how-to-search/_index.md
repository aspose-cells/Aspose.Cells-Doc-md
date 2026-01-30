———
title: How to use Search
description: Open the Search dialog to find values, formulas, or comments, then navigate or replace matches.
keywords: Search, Find what, Replace, Replace All, Look in, Match entire contents, Case Sensitive, Values, Formulas,
Comments
type: docs
weight: 1
url: /python-net/aspose-cells-gridjs/how-to-search
aliases:

- /python-net/aspose-cells-gridjs/how-to-find
- /python-net/aspose-cells-gridjs/how-to-replace
- /python-net/aspose-cells-gridjs/how-to-replace-all
- /python-net/aspose-cells-gridjs/how-to-search-comments
- /python-net/aspose-cells-gridjs/how-to-search-formulas

———

## Introduction

Search opens a dialog that lets you find text across Values, Formulas, or Comments, with options like Case Sensitive and
Match entire contents. You can move through matches with Next and Previous, and the current match is highlighted in the
grid. A separate Find & Replace view lets you replace a single match or all matches.

## How to use

1. Open Search from the toolbar or the Edit menu, or press Ctrl + F.
![](search-button.png)
2. In Find what, enter your text, then choose Look in (Values, Formulas, or Comments).

3. Optionally toggle Case Sensitive and Match entire contents, then click Next or Previous to navigate matches.

4. To replace, press Ctrl + H to open Find & Replace, enter Replace with, then use Replace or Replace All.
![](search-dialog.png)

## JavaScript API

xs = x_spreadsheet('#gridjs-demo-uid', option);

// Open Search (Find) dialog.
xs.sheet.modalSearch.show();

// Open Find & Replace dialog.
xs.sheet.modalSearch.show(true);

### Relevant functions

| Function | Description | Parameters | Returns |
|----------|-------------|------------|---------|
| sheet.modalSearch.show(showReplace) | Show the Search dialog; when showReplace is true, the Replace fields are shown
and Look in is hidden. | showReplace (boolean) | void |
| sheet.modalSearch.hide() | Close the Search dialog. | None | void |

sheet.modalSearch.show(showReplace) displays the Search UI and optionally the Replace UI based on the boolean parameter.
sheet.modalSearch.hide() closes the dialog and clears the current search highlight.

## Common Questions

Q: What can I search in?
A: The Search dialog supports Values, Formulas, and Comments via the Look in dropdown.

Q: How do I open Replace?
A: Use Ctrl + H (or call sheet.modalSearch.show(true)); the Replace fields appear and Look in is hidden.

Q: What happens if no matches are found?
A: The UI shows an info message indicating that nothing was found.
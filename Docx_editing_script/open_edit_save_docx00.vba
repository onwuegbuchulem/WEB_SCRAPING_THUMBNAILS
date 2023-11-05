Sub FindAndReplaceInFolder()
    Dim objDoc As Document
    Dim strFile As String
    Dim strFolder As String
    Dim strFindText As String
    Dim strReplaceText As String
    Dim alreadyReplaced As Boolean
    
    ' Pop up input boxes for the user to enter folder path, finding and replacing texts.
    strFolder = InputBox("Enter folder path here:")
    strFile = Dir(strFolder & "\" & "*.docx", vbNormal)
    
    strFindText = InputBox("Enter finding text here:")
    strReplaceText = InputBox("Enter replacing text here:")
    
    ' Loop through each file in the folder to search and replace texts. Save and close the file after the action.
    While strFile <> ""
        alreadyReplaced = False ' Reset the flag for each document
        
        Set objDoc = Documents.Open(FileName:=strFolder & "\" & strFile)
        
        With objDoc
            With .Content.Find
                .Text = strFindText
                .Replacement.Text = strReplaceText
                .Forward = True
                .Wrap = wdFindStop ' Stop searching after the first replacement
                .Execute Replace:=wdReplaceOne ' Replace only once
                If .Found = True Then
                    alreadyReplaced = True ' Set the flag to indicate replacement
                End If
            End With
            
            If alreadyReplaced Then
                objDoc.Save ' Save the document if a replacement was made
            End If
            
            objDoc.Close
        End With
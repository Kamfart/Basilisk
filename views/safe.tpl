<table>
<!-- Extract firt dict from list _data and get keys --> 
% head = list(_data[0])

<!-- Iterate on each keys to create dynamic th --> 
<tr>
    % for item in head:    
    <th>{{item}} </th>
    % end
</tr>


<!-- Iterate on each value of each dict to create dynamic td --> 
    % for item in _data:
    <tr>
        <td>{{item['Title']}} </td>
        <td>{{item['Username']}} </td>
        <td>{{item['Passwd']}} </td>
    </tr>
    % end
</table>
A = [0 0 1 1; 0 1 1 0; 0 0 0 0 ;0 1 1 0; 0 1 1 1 ];
result = [0 0 0 0; 0 0 0 0; 0 0 0 0; 0 0 0 0 ];
[row, col]=size(A);
current_cluster = 0;
for i= 1:row
    for j = 1:col
        element =A(i,j);
        
        if element == 1
            has_neigh = 0;
            % if element has top
            if i >1 
                if A(i-1,j) == 1
                    has_neigh = 1;

                    if result(i-1, j) < current_cluster
                        

                        current_cluster = result(i-1, j);
                        temp = j;
                        if (temp > 1)
                            
                            while (temp > 1 && A(i, temp-1) == 1)
                                result(i,temp-1) = current_cluster;
                                temp = temp -1;
                            end
                        end
                    end
                end
            end
         
            % else if element has left    
            if j>1
               
                if A(i,j-1) == 1
                    has_neigh = 1;


                end
            end
            % if has neigh on top or left
            if (has_neigh == 1)
                result (i,j)= current_cluster;
            else
                current_cluster = current_cluster + 1;
                result (i,j)= current_cluster;
            end
            
            
        end
    end
end

display(result)

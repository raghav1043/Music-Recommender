import java.util.*;
public static void main(String args[]){
	Scanner sc=new Scanner(System.in);
	int t=sc.nextInt();
	for(int test=0;test<t;test++){
		int n=sc.nextInt();
		int p=sc.nextInt();
		int arr[]=new int[n];
		int v[]=new int[n];
		for(int i=0;i<n;i++){
			arr[i]=sc.nextInt();
			v[i]=1<<i;
		}

		int a=Math.log(p)/Math.log(2);
		long ans[][]=new int[n][a];
		for(int i=0;i<n;i++){
			for(int j=0;j<a;j++){
				if(i==0){
					if(j==0){
						ans[i][j]=arr[0];
					}
					else{
						ans[i][j]=ans[i][j-1]+arr[i];
					}
				}
				else if(i<=j){
					ans[i][j]=Math.min(ans[i-1][j],ans[i][j-1]+arr[i]);
				}
				else{
					ans[i][j]=ans[i-1][j];
				}
			}
		}
		for(int i=0;i<n;i++){
			for(int j=0;j<a;j++){
				System.out.print(ans[i][j]+" ");
			}
			System.out.println();
		}

	}

}
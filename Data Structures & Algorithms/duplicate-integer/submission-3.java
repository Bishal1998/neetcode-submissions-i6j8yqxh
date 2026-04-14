class Solution {
    public boolean hasDuplicate(int[] nums) {

        // Map<Integer, Integer> map = new HashMap();

        // for (int i = 0; i< nums.length; i++){
        //     map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);

        //     if(map.get(nums[i]) >= 2){
        //         return true;
        //     }
        // }

        // return false;

        Set<Integer> set = new HashSet();

        for (int num : nums){
            if(set.contains(num)){
                return true;
            }

            set.add(num);
        }

        return false;
        
    }
}